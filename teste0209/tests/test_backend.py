from backend import processar_leitura


def test_processar_leitura_normaliza_sensor_e_retorna_status():
    resultado = processar_leitura("tm-01", 80.0)
    assert resultado == {
        "sensor_id": "TM-01",
        "temperatura": 80.0,
        "status": "ALERTA",
        "manutencao_recomendada": False,
    }


def test_leitura_critica_deve_recomendar_manutencao():
    resultado = processar_leitura("tm-02", 90.0)
    assert resultado["status"] == "CRITICO"
    assert resultado["manutencao_recomendada"] is True
