import pyautogui
import time

if __name__ == "__main__":
    for i in range(30):
        time.sleep(0.5)
        pos = pyautogui.position()
        print(pos)