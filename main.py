from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

#--------------------------------------------

def click(x,y):
    time.sleep(0.01)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.01)

#--------------------------------------------

clickCount = 0
cookiePos = [300, 450]
SugarLumpPos = [600, 130]

while keyboard.is_pressed('q') != True:
    click(cookiePos[0], cookiePos[1])
    clickCount += 1

    if clickCount > 1500:#Works every once in a while.

        click(SugarLumpPos[0], SugarLumpPos[1])#Clicks on sugerlump bc why not

        goldenCookie = pyautogui.locateOnScreen('cookie.png')#Finds if golden one exists
        if (goldenCookie != None):#Clicks on golden cookie and resets the var
            click(goldenCookie.left + 10, goldenCookie.top + 10)
            goldenCookie = None

        clickCount = 0#Resets the "timer"
        
#--------------------------------------------