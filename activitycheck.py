from pynput import keyboard, mouse
import threading
import time

score = 0
activity = False  # this flag tracks if there was any activity

# Lock for thread-safe access to the `activity` variable
lock = threading.Lock()

def on_key_press(key):
    global activity
    with lock:
        activity = True
    print(f"Key pressed: {key}")

def on_mouse_move(x, y):
    global activity
    with lock:
        activity = True
    print(f"Mouse moved to: {x}, {y}")

def score_updater():
    global score, activity
    while True:
        time.sleep(2)  # check every 2 seconds
        with lock:
            if activity:
                score += 1
                print(f"Activity detected. Score: {score}")
                activity = False  # reset for next check
            else:
                score -= 1
                print(f"No activity. Score: {score}")

# Start listeners
keyboard_listener = keyboard.Listener(on_press=on_key_press)
mouse_listener = mouse.Listener(on_move=on_mouse_move)
keyboard_listener.start()
mouse_listener.start()

# Start score tracking thread
score_thread = threading.Thread(target=score_updater)
score_thread.daemon = True  # exit when main program exits
score_thread.start()

keyboard_listener.join()
mouse_listener.join()
