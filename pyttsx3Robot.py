from pyttsx3 import *
import os

speak('Hello from IRAN')

speak('Do you want to open notepad?')
cmd = input()

if cmd == 'yes':
    os.system('notepad')

# github.com/Legendify/Python
