import os
from time import sleep

valor = True
flag = True

while valor:
    try:
        pergunta = input('Deseja ativar o sleep timer?: (s/n) ')
        if pergunta.lower() == 's':
            while flag:
                tempo = int(input('Por quanto tempo ele continuará ligado?: (Digite em segundos) '))
                if tempo <= 0:
                    print('-'*39)
                    print('Por favor, insira um valor MAIOR que 0!')
                    print('-'*39)
                else:
                    flag = False
                    valor = False
                    if tempo/60 > 9:
                        print(f'+{"-"*41}+\n|  O tempo definido foi de {tempo/60:.0f} minuto(s)!  |\n+{"-"*41}+\n')
                    else:
                        print(f'+{"-"*41}+\n|  O tempo definido foi de {tempo/60:.1f} minuto(s)! |\n+{"-"*41}+\n')
                    for i in range(tempo, 0, -1):
                        sleep(1)
                        if i == 10:
                            print(f'+{"-"*41}+\n|       Contagem regressiva iniciada!     |\n+{"-"*41}+')
                            sleep(0.5)
                            print(f'| Restam {i} segundos para o desligamento! |')
                        if i < 10:
                            print(f'| Restam {i} segundos para o desligamento!  |')
                    sleep(1)
                    print(f'+{"-"*41}+\n|   Obrigado por usar nosso aplicativo!   |\n+{"-"*41}+')
                    sleep(2)
                    os.system("shutdown /s /t 1")
        elif pergunta.lower() == 'n':
            print(f'+{"-"*41}+\n|           Você escolheu sair!           |\n+{"-"*41}+')
            sleep(2)
            valor = False
        else:
            print(f'+{"-"*41}+\n|      Por favor, insira "s" ou "n".      |\n+{"-"*41}+')
            sleep(1)
    except:
        print(f'+{"-"*41}+\n|      Por favor, insira "s" ou "n".       |\n+{"-"*41}+')
        sleep(1)