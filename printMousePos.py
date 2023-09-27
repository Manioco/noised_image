import pyautogui
import time

mouse_x, mouse_y = pyautogui.position()
time.sleep(4)
print(f"X: {mouse_x} | Y: {mouse_y}")
