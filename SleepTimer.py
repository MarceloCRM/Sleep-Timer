import os
from time import sleep
from datetime import datetime

hora_atual = datetime.now()
flag = True
while flag:
    try:
        tempo = input("Até que horas o computador ficará ligado? (HH:MM): ")
        try:
            hora_futura = datetime.strptime(f"{tempo}", "%H:%M").replace(year=hora_atual.year, month=hora_atual.month, day=hora_atual.day)
        except:
            hora_futura = datetime.strptime(f"{tempo}", "%H:%M:%S").replace(year=hora_atual.year, month=hora_atual.month, day=hora_atual.day)
        diferenca = int((hora_futura-hora_atual).total_seconds())
        if diferenca < 1:
            print(f"+{'-'*36}+\n| Por favor, insira uma hora futura! |\n+{'-'*36}+")
        else:
            flag = False
            message = f"|  O computador será desligado em {diferenca//60} minuto(s), às {str(hora_futura.time())}.  |"
            print(f"+{'-'*(len(message)-2)}+\n{message}\n+{'-'*(len(message)-2)}+") 
            for i in range(int(diferenca), 0, -1):
                message = f"Restam {i} segundos para o desligamento!"
                if i == 10:
                    print(f"+{'-'*41}+\n|       Contagem regressiva iniciada!     |\n+{'-'*41}+")
                    print(f"| {message.ljust(len("|       Contagem regressiva iniciada!     |")-4)} |")
                elif i < 10:
                    print(f"| {message.ljust(len("|       Contagem regressiva iniciada!     |")-4)} |")
                sleep(1)
            sleep(1)
            print(f"+{'-'*41}+\n|   Obrigado por usar nosso aplicativo!   |\n+{'-'*41}+")
            sleep(2)
            os.system("shutdown /s /t 1")
    except ValueError:
        print(f"\nErro: O formato não corresponde a HH:MM ou HH:MM:SS.\n")
        sleep(1)
    