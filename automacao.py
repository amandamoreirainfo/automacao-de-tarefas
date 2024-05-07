import pyautogui
import time

pyautogui.PAUSE =  2.0

pyautogui.press("win")
pyautogui.write("Opera")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


time.sleep(5)


#print(pyautogui.position())

pyautogui.click(x=737, y=451)
pyautogui.write("amandateste@gmail.com")
pyautogui.press("tab")
pyautogui.write("amandateste1")