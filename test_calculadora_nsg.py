import unittest
from calculadora_nsg import NSGCalculadora




class TestNSGCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora_nsg = NSGCalculadora()

    def test_adiciona_materia(self):
        self.calculadora_nsg.adiciona_materia(60, 70)
        self.assertEqual(len(self.calculadora_nsg.materias), 1)
        self.assertEqual(self.calculadora_nsg.materias[0], (4, 70))

        self.calculadora_nsg.adiciona_materia(30, 80)
        self.assertEqual(len(self.calculadora_nsg.materias), 2)
        self.assertEqual(self.calculadora_nsg.materias[1], (2, 80))
    
    def test_adiciona_materia_and_calcula_nsg(self):
        self.calculadora_nsg.adiciona_materia(60, 68)
        self.calculadora_nsg.adiciona_materia(60, 90)
        self.calculadora_nsg.adiciona_materia(60, 67)
        self.calculadora_nsg.adiciona_materia(90, 66)
        self.calculadora_nsg.adiciona_materia(60, 63)

        nsg = self.calculadora_nsg.calcula_nsg()
        self.assertAlmostEqual(nsg, 70.36, places=2)

    def test_nenhuma_materia(self):
        nsg = self.calculadora_nsg.calcula_nsg()
        self.assertEqual(nsg, 0)
    
    def test_uma_materia(self):
        self.calculadora_nsg.adiciona_materia(60, 70)
        nsg = self.calculadora_nsg.calcula_nsg()
        self.assertEqual(nsg, 70)

    def test_valores_invalidos(self):
        # horas negativas ou 0
        with self.assertRaises(ValueError):
            self.calculadora_nsg.adiciona_materia(-30, 70)
        with self.assertRaises(ValueError):
            self.calculadora_nsg.adiciona_materia(0, 70)
        # pontos negativos ou maiores que 100
        with self.assertRaises(ValueError):
            self.calculadora_nsg.adiciona_materia(30, -70)
        with self.assertRaises(ValueError):
            self.calculadora_nsg.adiciona_materia(30, 101)




if __name__ == '__main__':
    unittest.main()
        
        

