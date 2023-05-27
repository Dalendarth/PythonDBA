import psutil

# obtendo informação de uso da memoria
memoria = psutil.virtual_memory()
uso_total = memoria.total - memoria.available

# uso total de memoria ram
print(f'Uso total de memoria RAM: {uso_total / 1024 / 1024} MB')

# lista de processos consumindo RAM
processos = []
for proc in psutil.process_iter(['name', 'memory_info']):
    try:
        nome = proc.info['name']
        memoria = proc.info['memory_info'].rss
        processos.append((nome, memoria))
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# ordenando processos de acordo com o consumo de RAM
processos.sort(key=lambda x: x[1], reverse=True)

# listando os 5 apps que mais consomem RAM
print('Os 5 aplicativos que mais consomem memoria RAM: ')
for i, (nome, memoria) in enumerate(processos[:5]):
    print(f"(i+1). {nome}: {memoria / 1024 / 1024} MB")