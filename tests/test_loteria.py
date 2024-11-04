from lottery.loteria import gerar_jogo


def test_gerar_jogo():
    r = gerar_jogo()
    assert len(r) == 6 and all(isinstance(r[i], int) for i in range(6))
