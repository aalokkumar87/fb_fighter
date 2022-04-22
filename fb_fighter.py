import pyautogui
import time

file = open("gali.txt", "r")
gali = file.read().splitlines()

time.sleep(5)
for x in gali:
    pyautogui.typewrite(x)
    pyautogui.press("enter")
    time.sleep(2)
