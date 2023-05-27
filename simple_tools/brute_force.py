import subprocess
import winreg


def listar_programas_instalados():
    programas = []
    try:
        # Chave do Registro do Windows para os programas instalados
        chave_32bits = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
            0,
            winreg.KEY_READ | winreg.KEY_WOW64_32KEY
        )
        chave_64bits = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
            0,
            winreg.KEY_READ | winreg.KEY_WOW64_64KEY
        )

        def adicionar_programa(chave):
            try:
                valor_nome, _ = winreg.QueryValueEx(chave, "DisplayName")
                programas.append(valor_nome)
            except FileNotFoundError:
                pass

        # Loop pelas subchaves (programas instalados)
        for i in range(winreg.QueryInfoKey(chave_32bits)[0]):
            subchave_nome = winreg.EnumKey(chave_32bits, i)
            subchave = winreg.OpenKey(chave_32bits, subchave_nome)
            adicionar_programa(subchave)

        for i in range(winreg.QueryInfoKey(chave_64bits)[0]):
            subchave_nome = winreg.EnumKey(chave_64bits, i)
            subchave = winreg.OpenKey(chave_64bits, subchave_nome)
            adicionar_programa(subchave)

        winreg.CloseKey(chave_32bits)
        winreg.CloseKey(chave_64bits)
    except FileNotFoundError:
        pass

    return programas


def desinstalar_programa(programa):
    # Executa o comando para desinstalar o programa usando o nome exato
    comando = f'msiexec /x "{{{programa}}}"'
    subprocess.run(comando, shell=True)


def main():
    # Lista os programas de terceiros instalados
    programas = listar_programas_instalados()

    # Programas
    print("Programas de Terceiros Instalados:")
    for i, programa in enumerate(programas, 1):
        print(f"{i}. {programa}")

    # Pergunta ao usuário se deseja desinstalar algum programa
    opcao = input("Digite o número do programa que deseja desinstalar (ou '0' para sair): ")

    # Verifica se o usuário selecionou um número válido
    if opcao.isdigit() and int(opcao) in range(1, len(programas) + 1):
        programa_selecionado = programas[int(opcao) - 1]
        print(f"Desinstalando {programa_selecionado}...")
        desinstalar_programa(programa_selecionado)
        print(f"{programa_selecionado} foi desinstalado com sucesso!")
    elif opcao == '0':
        print("Encerrando o programa...")
    else:
        print("Opção inválida!")


if __name__ == '__main__':
    main()