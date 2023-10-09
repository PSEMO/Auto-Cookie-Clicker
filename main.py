import PySimpleGUI as psg

psg.theme('DarkAmber')   # Add a touch of color

#define layout
layout=[[psg.Text('Choose current app size (1080p)',size=(30, 1), font='Lucida',justification='left')],
        
        [psg.Combo(['Windowed full screen', '(top-left) Quarter of the screen', '(top-left) As small as possible'],
                    default_value='Windowed full screen', key='appSizeMode', size = (34, 1))],

        [psg.Text('Buy mode',size=(20, 1), font='Lucida',justification='left')],

        [psg.Combo(['Don\'t buy', 'Buy upgrades', 'Buy most bottom-right building'], 
                   default_value='Don\'t buy', key='buyType', size = (34, 1))],

        [psg.Button('START', font=('Times New Roman',12))],
        [psg.Text('(press Q to stop process)', font=('Times New Roman',8), justification='right', text_color='white')]]
#Define Window
win = psg.Window('Auto Cookie Clicker V2.0',layout)
#Read  values entered by user
button, selected=win.read()
print(button)
print(selected)

#win.close()

# _______            __________                      _______   _         ______
#(  ____ \ |\     /| \__   __/                      (  ____ \ ( (    /| (  __  \
#| )   ( | | )   ( |    ) (                         | (    \/ |  \  ( | | (  \  )
#| |       | |   | |    | |       ===============   | (__     |   \ | | | |   ) |
#| | ____  | |   | |    | |       ===============   |  __)    | (\ \) | | |   | |
#| | \_  ) | |   | |    | |       ===============   | (       | | \   | | |   ) |
#| (___) | | (___) | ___) (___                      | (____/\ | )  \  | | (__/  )
#(_______) (_______) \_______/                      (_______/ |/    )_) (______/

if(button == 'START'):

    from pyautogui import *
    import pyautogui
    import time
    import keyboard
    import win32api, win32con
    from PIL import ImageGrab
    from PIL import Image
    from functools import partial
    ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

    time.sleep(0.5)

    #--------------------------------------------

    def click(x,y):
        time.sleep(0.005)
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.005)

    #--------------------------------------------

    secondScreen = False
    buyType = 0#default is 0
    #0 means disabled
    #1 means buy the next upgrade in order.
    #2 means buy the building that is right at the bottom-right.
    appSizeMode = 2#default is 0
    #0 = position: top-left of the screen. size: as little as possible.
    #1 = position: top-left of the screen. size: quarter of the screen.
    #2 = windowed-full-screen.

    #--------------------------------------------

    if(selected['appSizeMode'] == '(top-left) As small as possible'):
        appSizeMode = 0
    if(selected['appSizeMode'] == '(top-left) Quarter of the screen'):
        appSizeMode = 1
    if(selected['appSizeMode'] == 'Windowed full screen'):
        appSizeMode = 2

    if(selected['buyType'] == 'Don\'t buy'):
        buyType = 0
    if(selected['buyType'] == 'Buy upgrades'):
        buyType = 1
    if(selected['buyType'] == 'Buy most bottom-right building'):
        buyType = 2

    #--------------------------------------------

    clickCount = 0

    ScreenPosSize = [0, 0, 0, 0]
    CookiePos = [0, 0]
    SugarLumpPos = [0, 0]
    BuyPos = [0, 0]

    cookieImg = Image.open('a.png')

    #mini mod
    if(appSizeMode == 0):

        GrayScale = False

        cookieImg = Image.open('cookie.png')
        
        ScreenPosSize = [1, 31, 276, 141]
        CookiePos = [45, 90]
        SugarLumpPos = [94, 68]
        
        if(buyType != 0):
            if(buyType == 1):
                BuyPos = [182, 62]
            else:
                BuyPos = [230, 170]
        else:
            BuyPos = CookiePos
    #--------------------------

    #quarter mod
    if(appSizeMode == 1):

        GrayScale = True

        cookieImg = Image.open('Mcookie.png')
        
        ScreenPosSize = [1, 31, 940, 507]
        CookiePos = [150, 240]
        SugarLumpPos = [310, 140]
        
        if(buyType != 0):
            if(buyType == 1):
                BuyPos = [670, 120]
            else:
                BuyPos = [800, 530]
        else:
            BuyPos = CookiePos
    #--------------------------

    #full size mod
    if(appSizeMode == 2):

        GrayScale = True

        cookieImg = Image.open('Bcookie.png')
        
        ScreenPosSize = [0, 23, 1903, 1057]
        CookiePos = [290, 450]
        SugarLumpPos = [597, 133]
        
        if(buyType != 0):
            if(buyType == 1):
                BuyPos = [1630, 120]
            else:
                BuyPos = [1760, 1070]
        else:
            BuyPos = CookiePos
    #--------------------------

    if secondScreen == True:
        ScreenPosSize[0] = ScreenPosSize[0] + 1920
        CookiePos[0] = CookiePos[0] + 1920
        SugarLumpPos[0] = SugarLumpPos[0] + 1920
        BuyPos[0] = BuyPos[0] + 1920

    #--------------------------------------------

    while keyboard.is_pressed('q') != True:
            click(CookiePos[0], CookiePos[1])
            clickCount += 1

            if clickCount > 250:#Works every once in a while.
                clickCount = 0#Resets the "timer"
                
                goldenCookie = pyautogui.locateOnScreen(cookieImg,
                    region = (ScreenPosSize[0], ScreenPosSize[1], ScreenPosSize[2], ScreenPosSize[3]),
                    grayscale = GrayScale)#Finds if golden one exists
                
                if (goldenCookie != None):

                    click(SugarLumpPos[0], SugarLumpPos[1])#Tries to harvest a sugerlump
                    click(BuyPos[0], BuyPos[1])#Tries to Buy a building
                    click(goldenCookie.left, goldenCookie.top)#Clicks on golden cookie

    #--------------------------------------------