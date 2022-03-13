import keyboard
import pyautogui
import math
import time

def icetime():
    time_sta = time.perf_counter()
    # 処理を書く（ここでは5秒停止する）
    # 時間計測終了
    time_end = time.perf_counter()
    # 経過時間（秒）
    tim = time_end- time_stajk

def getpow():
    return math.log(start_time, 2)

def main():
    HOTKEY = "ctrl" + "+"

    def move_cursor_right():
        pyautogui.move(50, 0)

    def move_cursor_left():
        pyautogui.move(-50,0)

    def move_cursor_up():
        pyautogui.move(0, -50)

    def move_cursor_down():
        pyautogui.move(0,50)

    keyboard.add_hotkey(HOTKEY + 'up', move_cursor_up)
    keyboard.add_hotkey(HOTKEY + 'down', move_cursor_down)
    keyboard.add_hotkey(HOTKEY + 'right', move_cursor_right)
    keyboard.add_hotkey(HOTKEY + 'left', move_cursor_left)

    keyboard.wait()

if __name__ == "__main__":
    main()
