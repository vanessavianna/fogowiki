

class Aventureiro:
    def __init__(self, nome, habilidade):
        """
        Inicializa a instância do cartão de aventureiro.

        :param nome: Nome do aventureiro.
        :param habilidade: Descrição da habilidade especial do aventureiro.
        """
        self.nome = nome
        self.habilidade = habilidade

    def usar_habilidade(self):
        """
        Método que representa o uso da habilidade especial do aventureiro durante o jogo.
        """
        print(f"{self.nome}: {self.habilidade}")

    def trocar_habilidades(self, outro_aventureiro):
        """
        Troca as habilidades especiais com outro aventureiro.

        :param outro_aventureiro: Instância de outro aventureiro.
        """
        self.habilidade, outro_aventureiro.habilidade = outro_aventureiro.habilidade, self.habilidade

# Exemplos de instância de cartões de aventureiro
aventureiro1 = Aventureiro("Explorador", "Pode se mover para qualquer terreno adjacente")
aventureiro2 = Aventureiro("Engenheiro", "Pode secar dois terrenos por ação")

# Exemplos de uso das habilidades especiais
aventureiro1.usar_habilidade()
aventureiro2.usar_habilidade()
