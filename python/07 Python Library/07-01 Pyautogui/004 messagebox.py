import pyautogui

messagebox1 = pyautogui.alert(text='내용입니다', title='제목입니다', button='OK')
print(messagebox1)

messagebox2 = pyautogui.confirm(text='내용입니다', title='제목입니다', buttons=['OK', 'Cancel'])
print(messagebox2)

messagebox3 = pyautogui.prompt(text='내용입니다', title='제목입니다', default='입력하세요')
print(messagebox3)

messagebox4 = pyautogui.password(text='내용입니다', title='제목입니다', default='입력하세요', mask='*')
print(messagebox4)