def calcular_desconto(preco: float | int, percentual: float | int) -> float:
    if preco < 0:
        raise ValueError("O preço não pode ser menor que zero.")

    if percentual < 0 or percentual > 100:
        raise ValueError("O percentual deve estar entre 0 e 100.")

    desconto = preco * (percentual / 100)
    preco_final = preco - desconto

    return round(preco_final, 2)


def main():
    resultado = calcular_desconto(150, 20)
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()

