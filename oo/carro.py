""" Doctests
    >>> motor = Motor()
    >>> motor.frear()
    0
    >>> motor.acelerar()
    1
"""

class Motor():
    def __init__(self, velocidade_inicial=0):
        self.velocidade = velocidade_inicial

    def acelerar(self):
        self.velocidade += 1
        return self.velocidade

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0
        return self.velocidade


class Direcao():
    def __init__(self, direcao_inicial="Norte"):
        self.direcao = direcao_inicial

    def girar_a_direita(self):
        if self.direcao == "Norte":
            self.direcao = "Leste"
            return self.direcao
        elif self.direcao == "Leste":
            self.direcao = "Sul"
            return self.direcao
        elif self.direcao == "Sul":
            self.direcao = "Oeste"
            return self.direcao
        self.direcao = "Norte"
        return self.direcao

    def girar_a_esquerda(self):
        if self.direcao == "Norte":
            self.direcao = "Oeste"
            return self.direcao
        elif self.direcao == "Oeste":
            self.direcao = "Sul"
            return self.direcao
        elif self.direcao == "Sul":
            self.direcao = "Leste"
            return self.direcao
        self.direcao = "Norte"
        return self.direcao


if __name__ == "__main__":
    motor = Motor(10)
    print(motor.velocidade)
    print(motor.acelerar())
    print(motor.frear())
    direcao = Direcao()
    print(direcao.direcao)
    print(direcao.girar_a_direita())
    print(direcao.girar_a_esquerda())
    print(direcao.girar_a_esquerda())
