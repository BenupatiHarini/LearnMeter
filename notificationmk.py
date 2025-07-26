from pynput import keyboard, mouse
from plyer import notification
import threading
import time

# Activity tracking variables
activity = False
last_active_time = time.time()

# Notification function
def alert_user():
    notification.notify(
        title="Are you focused?",
        message="We noticed no activity. Time to re-focus!",
        timeout=5
    )

# Event handlers
def on_key_press(key):
    global activity, last_active_time
    activity = True
    last_active_time = time.time()
    print(f"Key pressed: {key}")

def on_mouse_move(x, y):
    global activity, last_active_time
    activity = True
    last_active_time = time.time()
    print(f"Mouse moved to: {x}, {y}")

# Idle checker thread
def idle_checker():
    while True:
        time.sleep(5)  # check every 5 seconds
        idle_time = time.time() - last_active_time
        if idle_time >= 60:
            alert_user()

# Start listeners
keyboard_listener = keyboard.Listener(on_press=on_key_press)
mouse_listener = mouse.Listener(on_move=on_mouse_move)
keyboard_listener.start()
mouse_listener.start()

# Start idle check thread
idle_thread = threading.Thread(target=idle_checker)
idle_thread.daemon = True
idle_thread.start()

keyboard_listener.join()
mouse_listener.join()
