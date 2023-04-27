import pyautogui

# Conecta ao computador
pyautogui.FAILSAFE = False
pyautogui.moveTo(0, 0, duration=1)
pyautogui.click()

# Move o mouse
pyautogui.moveTo(500, 500, duration=1)
pyautogui.click()
