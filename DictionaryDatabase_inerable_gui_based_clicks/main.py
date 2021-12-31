import sqlite3
import pyautogui
import time
import clipboard
from pynput.keyboard import Key, Controller
import colorama


keyboard = Controller()


def refresh_Page():
    refreshed = pyautogui.locateOnScreen(
        'images/refresh/refresh.png', confidence=0.8)
    pyautogui.click(x=(refreshed[0]+15), y=(refreshed[1]+13))


def refresh_Check():
    a = pyautogui.locateOnScreen('images/refresh/window.png', confidence=0.5)
    b = pyautogui.locateOnScreen('images/refresh/windowC.png', confidence=0.5)
    if a or b:
        return True
    else:
        return False


def Refresh():
    a = 0
    process = False
    while not process:
        if a % 5 == 0:
            refresh_Page()
        process = refresh_Check()
        a += 1
        time.sleep(1)
    return True


def Write(data):
    a = pyautogui.locateOnScreen('images/keyboard.png', confidence=0.6)
    pyautogui.click(a[0], a[1]-30)
    pyautogui.write(f'{data}')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def copy():
    a = False
    while not a:
        try:
            Blue = pyautogui.locateOnScreen(
                'images/copyBlue.png', confidence=0.9)
            Black = pyautogui.locateOnScreen(
                'images/copyBlack.png', confidence=0.9)
            if Blue == None:
                a = Black[0:2]
            else:
                a = Blue[0:2]
            pyautogui.click(x=a[0]+15, y=a[1]+15)
            a = True
        except:
            continue


def removetext():
    a = pyautogui.locateOnScreen('images/cross.png', confidence=0.9)
    if a != None:
        pyautogui.click(a[0]+15, a[1]+10)


conn = sqlite3.connect('Dictionary.db')
c = conn.cursor()

c.execute('SELECT `key`, valueHin FROM dictionary')
data = c.fetchall()

for i, x in enumerate(data):
    if x[1] == None or x[1] == 'None':
        if i % 20 == 0:
            print(colorama.Fore.BLUE+f'{i} Refreshing...', end='')
            conn.close()
            Refresh()
            print(colorama.Fore.GREEN+f'Done', sep=colorama.Style.RESET_ALL)
        removetext()
        print(colorama.Fore.RED+f'{i} Writing...', '',
              sep=colorama.Style.RESET_ALL, end='')
        Write(f"{x[0]}")
        print(colorama.Fore.GREEN+f'Done / ',
              sep=colorama.Style.RESET_ALL, end='')
        print(colorama.Fore.RED+f'Copying...',
              sep=colorama.Style.RESET_ALL, end='')
        copy()
        print(colorama.Fore.GREEN+f'Done / ',
              sep=colorama.Style.RESET_ALL, end='')
        removetext()
        hindi = clipboard.paste()
        update = f"""Update dictionary set valueHin = '{hindi}' where id = {i+1}"""
        c.execute(update)
        conn.commit()
        print(colorama.Fore.BLUE+f'{i+1}-{x} : {hindi}',
              '', sep=colorama.Style.RESET_ALL)
        time.sleep(2)
conn.close()
