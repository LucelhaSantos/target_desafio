import json

# Exemplo de faturamento diário em JSON
faturamento = '''[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},  # Dia sem faturamento
    {"dia": 5, "valor": 0.0},  # Dia sem faturamento
    {"dia": 6, "valor": 26742.6612}
    # Adicione outros dias aqui
]'''

dados = json.loads(faturamento)

# Filtrando dias com faturamento
faturamento_dias = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Menor e maior valor
menor_faturamento = min(faturamento_dias)
maior_faturamento = max(faturamento_dias)

# Média mensal (desconsiderando dias sem faturamento)
media_mensal = sum(faturamento_dias) / len(faturamento_dias)

# Dias acima da média
dias_acima_da_media = len([dia for dia in faturamento_dias if dia > media_mensal])

# Resultados
print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
