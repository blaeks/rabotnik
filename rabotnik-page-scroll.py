#!/usr/bin/python3
import pyautogui;
import time;

time.sleep(3);

#time.sleep(3);
#pyautogui.moveTo(3101,584)

time.sleep(1);
pyautogui.scroll(4, x=3101, y=584);
time.sleep(3);
pyautogui.scroll(-12);
time.sleep(12);
pyautogui.scroll(3);

while True:
        pyautogui.scroll(4, x=3101, y=584);
        pyautogui.scroll(-12);
        pyautogui.scroll(3);
        pyautogui.scroll(4, x=3001, y=384);
        pyautogui.scroll(8);
        pyautogui.scroll(-16);
        pyautogui.scroll(8);
print('Thank you');