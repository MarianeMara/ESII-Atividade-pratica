import os
from calculadora_nsg import NSGCalculadora

def clear_screen():
    # Verifica o sistema operacional e executa o comando correspondente
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/Mac
        os.system('clear')

def main():
    calculadora_nsg = NSGCalculadora()

    print("Qual a quantidade de matérias que você cursou este semestre?")
    numero_materias = int(input())
    clear_screen() # Limpa a tela

    for i in range(numero_materias):
        print("Digite o número de HORAS da {}º matéria:".format(i + 1))
        horas = int(input())
        print("Digite a NOTA tirada na {}º matéria:".format(i + 1))
        nota = int(input())

        calculadora_nsg.adiciona_materia(horas, nota)
        clear_screen()  # Limpa a tela

    nsg = calculadora_nsg.calcula_nsg()
    print("Seu NSG nesse semestre foi: ", round(nsg, 2))

if __name__ == "__main__":
    main()
