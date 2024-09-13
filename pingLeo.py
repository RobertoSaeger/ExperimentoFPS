import subprocess
import time
import csv

def ping_e_gravar(host, tempo_segundos):
    """
    Função para realizar pings em um host e gravar os resultados em um arquivo CSV.

    Args:
        host (str): O endereço do host a ser pingado.
        tempo_segundos (int): O tempo total da execução em segundos.
    """

    with open('delay.csv', 'w', newline='') as csvfile:
        fieldnames = ['Tempo (s)', 'Ping (ms)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        inicio = time.time()

        while time.time() - inicio < tempo_segundos:
            output = subprocess.check_output(['ping', '-c', '1', host])
            output = output.decode('utf-8')

            # Extrair o tempo de ping da saída do comando (ajuste a expressão regular conforme necessário)
            import re
            ping_ms = re.search(r'time=(\d+.\d+)', output).group(1)

            writer.writerow({'Tempo (s)': round(time.time() - inicio, 2), 'Ping (ms)': ping_ms})

            time.sleep(1)

if __name__ == '__main__':
    host = 'saeger.com.br'
    tempo_segundos = int(input("Digite o tempo em segundos: "))
    ping_e_gravar(host, tempo_segundos)
