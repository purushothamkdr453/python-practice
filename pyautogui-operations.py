import pyautogui
import time

#print("Screen Size is : ", pyautogui.size())

#print("Current Position of the mouse is : ", pyautogui.position())

#print("Move to the certain position : ", pyautogui.moveTo(700,700,duration=1))

#print("Move relative to the current position : ", pyautogui.moveRel(100,100,duration=1))

#print("Scrolling : ", pyautogui.scroll(200))

#print("using hot keys : ", pyautogui.hotkey("ctrlleft","a"))

#print("Click: ", pyautogui.click(1000,1000))

#print("tyewrite: ", pyautogui.typewrite("Hello"))

#time.sleep(20)

#pyautogui.click(100,100)
#pyautogui.typewrite("Hello purushotham")


time.sleep(20)

pyautogui.moveTo(2000,2000,duration=1)
pyautogui.dragRel(100,0,duration=1)
pyautogui.dragRel(0,100,duration=1)
pyautogui.dragRel(-100,0,duration=1)
pyautogui.dragRel(0,-100,duration=1)
