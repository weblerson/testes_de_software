# Monitoramento Industrial

Uma indústria com sensores instalados em máquinas. O backend recebe a identificação do sensor e a temperatura atual. A aplicação classifica a leitura e indica quando existe uma condição crítica que recomenda manutenção.

## Regras

| Regra | Condição | Resultado |
| --- | --- | --- |
| Faixa válida | -20 °C até 150 °C | Aceitar leitura |
| Normal | -20 °C até 74,99 °C | NORMAL |
| Alerta | 75 °C até 89,99 °C | ALERTA |
| Crítico | 90 °C até 150 °C | CRITICO |
| Manutenção | Status CRITICO | True |
| Sensor | sensor_id obrigatório | Erro se vazio |

## Executando os testes

```
python -m pip install -r requirements.txt
python -m pytest -v
```

## Gerar relatório HTML

```
python -m pytest -v --html=relatorio_testes.html --self-contained-html
```
