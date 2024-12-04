import pyautogui
import time

# 모니터 - 화면 크기 출력
print(pyautogui.size())

# 마우스 - 위치 출력
time.sleep(2)
print(pyautogui.position())

# 마우스 - 정보 추출 GUI
pyautogui.mouseInfo()