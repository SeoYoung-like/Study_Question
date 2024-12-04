import pyautogui

# [참고] 주석 처리 단축키 : Ctrl + /

# 1) 마우스 - 이동
pyautogui.moveTo(33, 250)
pyautogui.moveTo(33, 250, 5)

# 2) 마우스 - 이동
pyautogui.moveRel(0, 300, 2)	# y가 300만큼 2초 동안 이동
pyautogui.moveRel(300, 0, 2)	# x가 300만큼 2초 동안 이동

# 3) 마우스 - 클릭
pyautogui.click()
pyautogui.click(button='right')
pyautogui.doubleClick()
pyautogui.click(clicks=3, interval=1) # 1초마다 3번 클릭

# 4) 마우스 - 드래그
# 1169,53 => 860,61
pyautogui.moveTo(1169, 53, 2)
pyautogui.dragTo(860, 61, 2)