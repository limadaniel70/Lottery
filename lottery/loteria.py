import random

# [1, 2, 3, ..., 60]
numeros_validos = list(range(1, 61))


def gerar_jogo() -> tuple[int, ...]:
    return tuple(random.choices(numeros_validos, k=6))
