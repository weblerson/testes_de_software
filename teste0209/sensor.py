def classificar_temperatura(temperatura: float) -> str:
    if temperatura < -20 or temperatura > 150:
        raise ValueError(
            "A temperatura deve estar entre -20 e 150 graus."
        )
    if temperatura >= 90:
        return "CRITICO"
    if temperatura >= 75:
        return "ALERTA"
    return "NORMAL"
