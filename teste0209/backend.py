from sensor import classificar_temperatura


def processar_leitura(sensor_id: str, temperatura: float) -> dict:
    if not isinstance(sensor_id, str) or not sensor_id.strip():
        raise ValueError("O sensor_id deve ser informado.")
    status = classificar_temperatura(temperatura)
    return {
        "sensor_id": sensor_id.strip().upper(),
        "temperatura": float(temperatura),
        "status": status,
        "manutencao_recomendada": status == "CRITICO",
    }
