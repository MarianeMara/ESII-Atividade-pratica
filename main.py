from calculadora_nsg import NSGCalculadora

def main():

    calculadora_nsg = NSGCalculadora()

    print("Qual a quantidade de matérias que você cursou este semestre?")

    numero_materias = int(input())

    for i in range(numero_materias):
        print("Digite o número de HORAS da {}º materia:" .format(i + 1))
        horas = int(input())
        print("Digite a NOTA tirada na {}º materia:" .format(i + 1))
        nota = int(input())

        calculadora_nsg.adiciona_materia(horas, nota)

    nsg = calculadora_nsg.calcula_nsg()
    print("Seu NSG nesse semestre foi: ", round(nsg, 2))

if __name__ == "__main__":
    main()
