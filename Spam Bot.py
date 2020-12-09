import pyautogui, time
time.sleep(5)
f = open("Hello", 'r')
for word in f:
       pyautogui.typewrite(word)
       pyautogui.press("enter")