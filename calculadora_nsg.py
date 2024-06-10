class NSGCalculadora:
    def __init__(self):
        self.materias = []

    def adiciona_materia(self, horas, pontos):
        creditos = horas / 15
        self.materias.append((creditos, pontos))

    def calcula_nsg(self):
        total_pontos = sum(creditos * pontos for creditos, pontos in self.materias)
        total_creditos = sum(creditos for creditos, pontos in self.materias)
        if total_creditos == 0:
            return 0
        return total_pontos / total_creditos
