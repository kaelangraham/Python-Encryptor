import pyautogui
import keyboard
import time
import pyperclip

def encrypt() -> None:
    # copys all text to clipboard
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    text: str = pyperclip.paste()

    # encrypts text
    

keyboard.wait('ctrl+shift+e')
