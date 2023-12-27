# teste_cartase4.py

import unittest
from fogo.ilha import IlhaProibida

class TesteCartasTabuleiro(unittest.TestCase):

    def test_contacartas(self, terrenos= None):
        # importar de cartas de tabuleiro de IlhaProibida em uma lista

        self.assertEqual(24, len(IlhaProibida().terrenos))  # add assertion here

if __name__ == '__main__':
    unittest.main()
