import pyautogui as gui
import pyperclip
import time
import settings
import keywords
import positions as p
import re

def exhibition(text):
    gui.mouseUp()
    gui.moveTo(p.notepad_x, p.notepad_y, 1, gui.easeInOutQuad)
    gui.mouseDown()
    gui.click()
    gui.press('enter')
    gui.typewrite(text, interval=0.05)

def clean_input():
    gui.mouseDown()
    gui.hotkey('ctrl', 'a')
    gui.hotkey('delete')
    gui.mouseUp()

def input_date(j):
    gui.mouseUp()
    gui.moveTo(p.window_x, p.window_y, 0.5)
    gui.click()
    for _ in range(17):
        gui.hotkey('tab')
    # clean_input()
    datelist = [j+1970, 1, 1, j+1970, 12, 31]
    for elem in datelist:
        gui.hotkey('tab')
        gui.hotkey('ctrl', 'a')
        gui.press('delete')
        gui.typewrite(str(elem))
    time.sleep(0.1)
    gui.press('enter')

def input_sheet():
    gui.mouseUp()
    gui.moveTo(p.res_x1, p.res_y1, 0.3, gui.easeInOutQuad)
    gui.mouseDown()
    gui.dragTo(p.res_x2, p.res_y2, 0.5)
    gui.hotkey('ctrl', 'c')
    text = pyperclip.paste()
    text = re.sub(r"\D", "", text)
    print(text)
    gui.moveTo(p.sheet_x, p.sheet_y, 0.5)
    gui.click()
    gui.typewrite(str(text))
    time.sleep(0.3)
    gui.press('enter')

def list_init():
    gui.moveTo(p.sheet_x, p.sheet_y, 1)
    gui.mouseDown()
    gui.click()
    start = time.time()
    while time.time() - start < 7:
        gui.press('up')
    gui.press('right')
    gui.press('down')   
    gui.mouseUp()

if __name__ == "__main__":
    gui.press("nonconvert")
    for i in keywords.KeyWordList:
        for j in range(51):
            # exhibition('')
            # exhibition('1. Input search keywords')
            gui.scroll(100)
            gui.moveTo(p.window_x, p.window_y, 0.5, gui.easeInOutQuad)
            clean_input()
            gui.mouseDown()
            pyperclip.copy(i)
            gui.hotkey('ctrl', 'v')

            # exhibition('2. Input the target period')
            input_date(j)
            gui.press('enter')

            exhibition('3. Waiting for page transition......')
            exhibition('4. Input the number of the search to Excel sheet')
            input_sheet()

            gui.moveTo(p.window_x, p.window_y, 0.4)
            gui.mouseDown()
            gui.hotkey('alt', 'left')
        
            if j == 50:
                gui.mouseUp()
                list_init()
