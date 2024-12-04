import pyautogui
import pyperclip

# 영문 - 타이핑 ( write 함수 )
pyautogui.write("hello king!") # 괄호 안의 문자를 타이핑 합니다.
pyautogui.write('hello world!', interval=0.1) # 각 문자를 0.25마다 타이핑합니다. 

# 한글 - 타이핑 ( pyperclip  - 복사 붙여넣기 )
pyperclip.copy("안녕하세요") # 클립보드에 텍스트를 복사합니다. 
pyautogui.hotkey('ctrl', 'v') # 붙여넣기 (hotkey 설명은 아래에 있습니다.)

# 키보드 - 단축키
pyautogui.press('shift', presses=5, interval=1) # shift 키를 누릅니다.
pyautogui.press('ctrl') # ctrl 키를 누릅니다. 
