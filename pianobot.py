# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:57:43 2020

@author: Hitesh
"""

import pyautogui
from pyautogui import *
import time
import keyboard
import win32api,win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
xarr=[325,450,550,725]
while keyboard.is_pressed("h")==False:
    
    for x in xarr:
        if pyautogui.pixel(x,500)[1]>240:
            click(x,500)
    