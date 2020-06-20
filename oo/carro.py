""" Doctests
    >>> motor = Motor()
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> direcao = Direcao()
    >>> direcao.girar_a_direita()
    >>> direcao.direcao
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.direcao
    'Norte'
"""
NORTE = 'Norte'
LESTE = 'Leste'
OESTE = 'Oeste'
SUL = 'Sul'

class Motor():
    def __init__(self, velocidade_inicial=0):
        self.velocidade = velocidade_inicial

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0,self.velocidade)


class Direcao():
    rotaciona_direita_dict = {NORTE:LESTE,LESTE:SUL,SUL:OESTE,OESTE:NORTE}
    rotaciona_esquerda_dict = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.direcao = NORTE

    def girar_a_direita(self):
        self.direcao = self.rotaciona_direita_dict[self.direcao]

    def girar_a_esquerda(self):
        self.direcao = self.rotaciona_esquerda_dict[self.direcao]


if __name__ == "__main__":
    pass
