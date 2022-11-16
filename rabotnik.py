#!/usr/bin/python3
#from curses import ACS_DARROW
import pyautogui;
import time;
import curses;

time.sleep(3);

#Move to Refresh
#pyautogui.moveTo(3439,135); - on 16nov2022_I had to update
pyautogui.moveTo(3397,130);

#Refresh CLICK(!)
time.sleep(3);
pyautogui.click();

#Move to AllCampaigns [ Point(x=2008, y=193) ] & Click
time.sleep(3);
pyautogui.click(2008,193);


#Keyboard INPUT position:
#Point(x=3200, y=132)

#Go to Search 
time.sleep(3);
pyautogui.click(3200,132);

#Keyboard Entry & select - Go To Keywords (!)
time.sleep(3);
pyautogui.typewrite('Keywords');
time.sleep(6);
#pyautogui.keyDown()
pyautogui.click(2723,165);

#reset filter - TODO -needs detection
#time.sleep(3);
#pyautogui.click()

#CLICK "Add filter"
time.sleep(5);
pyautogui.click(2662,474);

#TYPEWRITE "Status"
time.sleep(3);
pyautogui.typewrite('Status');

#Select "Status" in Filter
time.sleep(3);
pyautogui.click(2626,566);

#select "Eligible"
time.sleep(3);
pyautogui.click(2600,621);

#select "Eligible (Limited)""
time.sleep(3);
pyautogui.click(2598,659);

#Click "Apply"
time.sleep(3);
pyautogui.click(2726,850);

