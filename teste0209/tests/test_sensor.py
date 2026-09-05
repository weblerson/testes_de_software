import pytest

from sensor import classificar_temperatura


@pytest.mark.parametrize(
    "temperatura, esperado",
    [
        (-20.0, "NORMAL"),
        (0.0, "NORMAL"),
        (74.99, "NORMAL"),
        (75.0, "ALERTA"),
        (89.99, "ALERTA"),
        (90.0, "CRITICO"),
        (150.0, "CRITICO"),
    ],
)
def test_classificar_temperatura_cenarios_e_limites(temperatura, esperado):
    resultado = classificar_temperatura(temperatura)
    assert resultado == esperado


@pytest.mark.parametrize("temperatura", [-20.01, 150.01])
def test_temperatura_fora_da_faixa_deve_gerar_erro(temperatura):
    with pytest.raises(ValueError, match="temperatura"):
        classificar_temperatura(temperatura)
