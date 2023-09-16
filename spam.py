#to spam any given text
import pyautogui
import time
import webbrowser
url= input("Enter a url: ")
webbrowser.open(url)
time.sleep(5)
x = 'i can spam anything'
for i in range(5):
    pyautogui.write(x)
    pyautogui.press('enter')


#to spam from any given file
import pyautogui
import time
import webbrowser
url= input("Enter a url: ")
webbrowser.open(url)
time.sleep(5)
x = open("file", "r") #here "file" represents the given file
for words in x:
    pyautogui.write(words)
    pyautogui.press('enter')
