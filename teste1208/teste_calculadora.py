import pytest

from calculadora import calcular_desconto

@pytest.mark.parametrize(
    "preco,percentual,esperado",
    [
        (200, 10, 180),
        (150, 20, 120),
        (99.9, 0, 99.9),
        (100, 100, 0),
    ],
)
def test_calcular_desconto_cenarios_validos(preco: float | int, percentual: float | int, esperado: float):
    resultado = calcular_desconto(preco, percentual)

    assert resultado == esperado


@pytest.mark.parametrize("percentual", [-1.0, 101.0])
def test_percentual_invalido_deve_gerar_erro(percentual):
    with pytest.raises(ValueError, match="percentual"):
        calcular_desconto(100.0, percentual)

def test_preco_negativo_deve_gerar_erro():
    with pytest.raises(ValueError, match="preço"):
        calcular_desconto(-50.0, 10.0)

