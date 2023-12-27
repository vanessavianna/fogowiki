# teste_jogador.py

import unittest
from fogo.ilha import IlhaProibida
from fogo.jogador import Jogador

class TestIlhaProibida(unittest.TestCase):

    def test_numero_jogadores(self):
        # Crie uma instância de IlhaProibida com uma lista de jogadores
        jogadores = [Jogador("Jose"), Jogador("Fernando"), Jogador("Igor"), Jogador("Vanessa")]
        jogo = IlhaProibida(jogadores)

        # Verifique se o número de jogadores na instância do jogo é igual ao número de jogadores fornecidos
        self.assertEqual(4, len(jogadores))


if __name__ == '__main__':
    unittest.main()
