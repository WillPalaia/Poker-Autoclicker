import pyautogui
import time
import random

time.sleep(3)

while True:
    time.sleep(random.randrange(2))
    # if (pyautogui.pixelMatchesColor(740, 500, (255, 255, 255), tolerance=10)):
    # post flop
    for loc in pyautogui.locateAllOnScreen("check.png", confidence=.9):
        pyautogui.click(loc[0], loc[1])
    for loc in pyautogui.locateAllOnScreen("fold1.png", confidence=.9):
        pyautogui.click(loc[0], loc[1])
    for loc in pyautogui.locateAllOnScreen("fold2.png", confidence=.9):
        pyautogui.click(loc[0], loc[1])
    for loc in pyautogui.locateAllOnScreen("buyin.png", confidence=.9):
        pyautogui.click(loc[0], loc[1])
    # else:
    #     # pre flop
    #     for loc in pyautogui.locateAllOnScreen("check.png", confidence=.9):
    #         pyautogui.click(loc[0], loc[1])
    #     for loc in pyautogui.locateAllOnScreen("call.png", confidence=.9):ZX
