from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pyscreenshot
#y: 950 x: 550, 600, 700, 800
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.015)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q')==False:
    try:
        if pyautogui.pixel(600,500)==(0,0,0):
            click(600,500)
        if pyautogui.pixel(700,500)==(0,0,0):
            click(700,500)
        if pyautogui.pixel(800,500)==(0,0,0):
            click(800,500)
        if pyautogui.pixel(550,500)==(0,0,0):
            click(550,500)
    except:
        continue