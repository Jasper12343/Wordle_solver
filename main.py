import pyautogui
import time
import keyboard
import threading
import win32api
import win32con
import numpy as np
from PIL import Image

# Define the letters grid
letters = [
    ['g', 'l', 'e', 'n', 't'],
    ['b', 'r', 'i', 'c', 'k'],
    ['j', 'u', 'm', 'p', 'y'],
    ['v', 'o', 'z', 'h', 'd'],
    ['w', 'a', 'q', 'f', 's']
]

not_in_word = []
yellow_in_word = []
green_in_word = []

# Colors in RGB format
grey = (167, 174, 194)
green = (137, 181, 95)
yellow = (232, 195, 85)

def get_pixel_color(x, y):
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((x, y))
    return pixel_color

def on_triggered_test():
    temp_x = 825
    temp_y = 230
    for a in range(5):
        for i in range(5):
            print("\n")
            # First letter
            x, y = temp_x, temp_y
            pixel_color = get_pixel_color(x, y)
            print(f"Color of pixel at ({x}, {y}): {pixel_color}")
            temp_x = temp_x + 60
            if pixel_color == grey:
                print("Pixel color is grey")
                not_in_word.append(letters[a][i])
            elif pixel_color == green:
                print("Pixel color is green")
                green_in_word.append(letters[a][i])
            elif pixel_color == yellow:
                print("Pixel color is yellow")
                yellow_in_word.append(letters[a][i])
            else:
                print("Pixel color does not match any expected color")

            yellow_in_word.append("")
            green_in_word.append("")
            print(i)
            print(letters[a][i])
        temp_y = temp_y + 60
        temp_x = 825
    print(f"not {not_in_word}")
    print(f"yellow {yellow_in_word}")
    print(f"green {green_in_word}")

def on_triggered():
    time.sleep(0.5)
    pyautogui.write('glent', interval=0.025)
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.25)
    pyautogui.write('brick', interval=0.025)
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.25)
    pyautogui.write('jumpy', interval=0.025)
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.25)
    pyautogui.write('vozhd', interval=0.025)
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.25)
    pyautogui.write('waqfs', interval=0.025)
    time.sleep(0.2)
    pyautogui.press('enter')
    pyautogui.scroll(10)

def click_mouse():
    while not keyboard.is_pressed('§'):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0)  # Adjust sleep time if necessary

def on_triggered_auto_clicker():
    click_thread = threading.Thread(target=click_mouse)
    click_thread.start()
    click_thread.join()

def start():
    with open("word_list.txt", "r") as f:
        text = f.read()
        word_list = text.split('\n')
    i = "glent"
    if i in word_list:
        print(f"{i} in word list")
    keyboard.add_hotkey('ctrl+shift+alt+p', on_triggered)
    keyboard.add_hotkey('ctrl+shift+alt+o', on_triggered_test)
    keyboard.add_hotkey('ctrl+shift+alt+ü', on_triggered_auto_clicker)
    keyboard.wait('esc')

if __name__ == '__main__':
    start()
