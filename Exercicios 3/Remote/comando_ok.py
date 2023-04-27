import pyautogui

# Define o endereço IP do computador
REMOTE_PC_IP = '192.168.1.100'

# Conecta ao computador
pyautogui.FAILSAFE = False
pyautogui.moveTo(0, 0, duration=1)
pyautogui.click()

# Move o mouse
pyautogui.moveTo(500, 500, duration=1)
pyautogui.click()

# Envia uma sequência de caracteres no computador remoto
pyautogui.hotkey('ctrl', 'alt', 't')
pyautogui.typewrite('echo "Hello World!"')
pyautogui.press('enter')

# Encerra a conexão
pyautogui.hotkey('ctrl', 'd')
