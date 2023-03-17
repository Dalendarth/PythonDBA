import sys
import os
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout



def reconhecer_fala():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as fonte_audio:
        audio = reconhecedor.listen(fonte_audio)
    try:
        texto = reconhecedor.recognize_google(audio, language='pt-BR')
        return texto
    except:
        return "Não foi possível entender a fala"

def reconhecer(caixa_texto=3):
    texto = reconhecer_fala()
    caixa_texto.setText(texto)



class Janela(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.reconhecer_botao = QPushButton('Reconhecer voz', self)
        self.reconhecer_botao.move(20, 20)
        self.reconhecer_botao.clicked.connect(reconhecer)

        self.caixa_texto = QTextEdit(self)
        self.caixa_texto.setGeometry(20, 60, 360, 280)

        self.setGeometry(300, 300, 400, 360)
        self.setWindowTitle('Reconhecimento de voz')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Janela()
    sys.exit(app.exec_())