import pyautogui
import time
import random

def mouse_jiggler(interval=5, duration=60):
    end_time = time.time() + duration
    print(f"Starting mouse jiggler for {duration} seconds.")

    while time.time() < end_time:
        current_x, current_y = pyautogui.position()

        new_x = current_x + random.choice([-30, 30])
        new_y = current_y + random.choice([-30, 30])

        pyautogui.moveTo(new_x, new_y, duration=0.2)
        print(f"Mouse moved to ({new_x}, {new_y})")

        time.sleep(interval)

    print("Mouse jiggler finished.")

if __name__ == "__main__":
    mouse_jiggler(interval=5, duration=60)