import speech_recognition as sr
import pyautogui
# Se tratam de bibliotecas novas para mim, deixei observações nesse codigo
# Reconhecimento da voz
r = sr.Recognizer()

# Mic p/ entrada
mic = sr.Microphone()


palavraChave = "destravar"

def destravar_tela():
    pyautogui.press('esc')

# Loop para ouvir o mic e aguardar a palavra chave
while True:
    with mic as source:
        print("Aguardando palavra-chave...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:

        texto = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {texto}")
        if texto.lower() == palavraChave.lower():
            destravar_tela()
            print("Tela destravada!")
            break
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print(f"Não foi possível se comunicar com o serviço de reconhecimento de voz: {e}")