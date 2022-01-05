import pyautogui
import time

if __name__ == "__main__":
    pyautogui.press('win') #windowsキーを押す。
    time.sleep(1)
    pyautogui.typewrite('microsoft edge')
    pyautogui.press('enter') #ブラウザ起動
    time.sleep(4)
    pyautogui.moveTo(420, 420) #検索のテキストボックスにカーソル移動
    pyautogui.click()
    time.sleep(4)
    pyautogui.typewrite('pyautogui')
    pyautogui.press('enter')

# 検索ウィンドウ：1094, 442
# 検索ボタン：1804, 442
# 時期：1284, 826 / 1613, 826