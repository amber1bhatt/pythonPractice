##CTRL + SHIFT + B <-- WHEN NO INPUT FROM USER
##OTHERWISE USE BELOW
##Select all CTRL + ENTER
##Or CRTL + ` and run from terminal
##ALT + SHIFT + T for new terminal
##Run from CMD
    ##cd C:\Users\amber\OneDrive\Desktop\Programming\pythonPractice
    ##name_of_file.py

##https://pyautogui.readthedocs.io/en/latest/cheatsheet.html

import pyautogui

print(pyautogui.position()) #Position of mouse
print(pyautogui.size()) #Screen resolution
print(pyautogui.onScreen(10,10)) #true if x & y are within the screen
pyautogui.moveTo(130,100,duration=1.0)
pyautogui.FAILSAFE = False
#pyautogui.moveRel(xOffset=None,yOffset=None,duration=3.0) # move mouse relative to its current Position
#pyautogui.dragTo(200,20,duration=0.0) # drag mouse to x,y
#pyautogui.dragRel(xOffset=0,yOffset=0,duration=0.0) # drag mouse relative to current position

pyautogui.click(x=50,y=100,clicks=0,interval=1.0,button='left')
pyautogui.click(x=130,y=100,clicks=0,interval=1.0,button='left')
# for i in range(3,6):
#     pyautogui.typewrite("for j in range(1,2):\npyautogui.typewrite(""for k in range(1,2),interval=0.5"")\n",interval=0.01)

# for i in range(1,10):
#     pyautogui.typewrite("#Jasper is a hater" + "\n", interval=0.05)
