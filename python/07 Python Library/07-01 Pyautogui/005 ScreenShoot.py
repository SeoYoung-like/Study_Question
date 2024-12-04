import pyautogui as pg

# 방법1 
button5location = pg.locateOnScreen("C:\\4.jpg") 
point = pg.center(button5location)
pg.click(point)

# 방법2
point = pg.locateCenterOnScreen("C:\\4.jpg")
pg.click(point)