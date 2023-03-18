import speech_recognition as sr
import pyautogui
import os

r = sr.Recognizer()

mic = sr.Microphone()

destravar_palavra_chave = "destravar"
travar_palavra_chave = "travar"

def destravar_tela():
    pyautogui.press('esc')

def travar_maquina():
    os.system("rundll32.exe user32.dll, LockWorkStation")

# Loop para ouvir o mic e aguardar a palavra chave
while True:
    with mic as source:
        print("Aguardando palavra-chave...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {texto}")
        if texto.lower() == destravar_palavra_chave.lower():
            destravar_tela()
            print("Tela destravada!")
        elif texto.lower() == travar_palavra_chave.lower():
            travar_maquina()
            print("Máquina travada!")
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print(f"Não foi possível se comunicar com o serviço de reconhecimento de voz: {e}")