from pynput import keyboard, mouse

def on_key_press(key):
    print(f"Key pressed: {key}")

def on_mouse_move(x, y):
    print(f"Mouse moved to: {x}, {y}")

keyboard_listener = keyboard.Listener(on_press=on_key_press)
mouse_listener = mouse.Listener(on_move=on_mouse_move)

keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()   

