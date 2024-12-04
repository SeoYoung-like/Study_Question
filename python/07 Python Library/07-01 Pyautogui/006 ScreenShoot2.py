import pyautogui as pg


pg.screenshot("1.png", region=[1384, 664, 60, 30])

point = pg.locateCenterOnScreen("1.png")
pg.click(point)