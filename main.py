git branch -m master main
git push -u origin main

# radia.fogo.main.py
# __authors__ Fernanda, Finn, Vanessa, Anderson 
"""Página de Entrada do jogo Ilha Proibida Equipe Fogo.

WORKFLOWY - http://bit.ly/Dev_Agile_23

EQUIPE FOGO 

.. codeauthor:: Fernanda Araujo <fernandacsaraujo@gmail.com>
.. codeauthor:: Finn Kockelke <finn_kockelke@gmx.net>
.. codeauthor:: Vanessa M Vianna <vanmvianna@gmail.com>
.. codeauthor:: Anderson Amorim da Silva <anderson.amorix@gmail.com>


Changelog
---------
.. versionadded::    23.11
    Divisão de equipes (07).
    Adicao do modulo ilha e jogador.
    
.. versionadded::    23.10
    Classes Ilha, Terreno, Peao (10).
    
.. versionadded::    23.09
    Versão Inicial (26).

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023, Fernanda Araujo** <fernandacsaraujo@gmail.com>, Finn Kockelke** <finn_kockelke@gmx.net>, Vanessa M Vianna** <vanmvianna@gmail.com>
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""

from fogo.ilha import IlhaProibida as Ilha
from fogo.jogador import Jogador
from fogo.peao import Peao
from fogo.aventureiro import Aventureiro


if __name__ == "__main__":
    jogadores = [
        Jogador("Jose"),
        Jogador("Fernando"),
        Jogador("Igor"),
        Jogador("Vanessa")
    ]
    Ilha(jogadores)

    Peao()
    Aventureiro("Explorador", "Pode se mover para qualquer terreno adjacente")
