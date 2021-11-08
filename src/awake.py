import pyautogui
import time
import sys
from datetime import datetime
import time
import keyboard
import random
import win32api, win32con
pyautogui.FAILSAFE = False
numMin = None

#   Exit x=29 y=99 
#   Confirm x=1095 y=228 
#   Continue x=1824 y=485 
#   Next x=1241 y=179 


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 3
else:
    numMin = int(sys.argv[1])
while(True):
    # pyautogui.displayMousePosition()
    x=0
    while(x<numMin):
        print('start')

        time.sleep(60)
        print('slept 60')
        x+=1
        click(29, 99)
        print('click exit')
        time.sleep(5)
        click(1095,228)
        print('click confirm')
        time.sleep(5)
        click(1824, 485)
        time.sleep(5)
        click(1824, 485)
        print('go back')
        time.sleep(5)
        click(1241, 179)
        print('next')
        time.sleep(5)

    # for i in range(0,200):
    #     pyautogui.moveTo(0,i*4)
    # pyautogui.moveTo(1,1)
    # for i in range(0,3):
    #     pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))