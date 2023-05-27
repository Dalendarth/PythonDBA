import psutil
import subprocess


# obtendo temperatura cpu em linux
def obter_temperatura_cpu_linux():
    output = subprocess.check_output(['sensors'])
    output = output.decode('utf-8')
    for line in output.split('\n'):
        if 'Core 0: ' in line:
            temperatura = line.split(':')[1].split()[0]
            return float(temperatura)

    return None


# obtendo temperatura cpu em windows
def obter_temperatura_cpu_windows():
    output = subprocess.check_output(['wmic', 'cpu', 'get', 'Temperature'])
    output = output.decode('utf-8')
    linhas_temperatura = output.strip().split('\n')[:1]
    temperatura = int(linhas_temperatura[0]) / 10.0
    return temperatura


# temp processador
def obter_temperatura_cpu():
    try:
        if psutil.WINDOWS:
            return obter_temperatura_cpu_windows()
        elif psutil.LINUX:
            return obter_temperatura_cpu_linux()
        else:
            return None
    except(subprocess.SubprocessError, FileNotFoundError, IndexError):
        return None


# listando proc. e utiliz. da cpu
def obter_utilizacao_cpu():
    processos = []
    for proc in psutil.process_iter(['name', 'cpu_percent']):
        try:
            nome = proc.info['name']
            uso_cpu = proc.info['cpu_percent']
            processos.append((nome, uso_cpu))
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    processos.sort(key=lambda x: x[1], reverse=True)
    return processos


# obtendo indice de integridade do processador
def obter_integridade_cpu(temperatura):
    if temperatura is None:
        return "Desconhecido"
    elif temperatura < 50:
        return "Normal"
    elif temperatura < 90:
        return "Aquecendo"
    else:
        return "Risco"


# obt. Temp_cpu
temperatura = obter_temperatura_cpu()

# most. temp. cpu

print(f'Temperatura do processador: {temperatura}ºC')

# lista de processos e uso deles na cpu
processos = obter_utilizacao_cpu()

# listando programas demandando alto nivel de capacidade logica
print('Programas que mais estão demandando capacidade logica computacional: ')
for i, (nome, uso_cpu) in enumerate(processos[:5]):
    print(f'{i + 1}. {nome}: {uso_cpu}%')

# obtendo e mostrando integridade do processador
indice_integridade = obter_integridade_cpu(temperatura)
print(f'Indice de integridade do processador: {indice_integridade}')
