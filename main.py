from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

#--------------------------------------------

def click(x,y):
    time.sleep(0.005)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.005)

#--------------------------------------------

cookiePos = [300, 450]
SugarLumpPos = [600, 130]
Building = [1750, 990]

#--------------------------------------------

clickCount = 0

while 1:
    if keyboard.is_pressed('q') != True:
        click(cookiePos[0], cookiePos[1])
        clickCount += 1

        if clickCount > 2000:#Works every once in a while.
            clickCount = 0#Resets the "timer"

            goldenCookie = pyautogui.locateOnScreen('cookie.png')#Finds if golden one exists
            if (goldenCookie != None):
                click(SugarLumpPos[0], SugarLumpPos[1])#Tries to harves a sugerlump
                click(Building[0], Building[1])#Tries to Buy a building
                click(goldenCookie.left, goldenCookie.top)#Clicks on golden cookie
#--------------------------------------------
