import json

# Exemplo de dados de faturamento em JSON
faturamento_diario = '''{
    "dias": [
        {"dia": 1, "valor": 1000.0},
        {"dia": 2, "valor": 2000.0},
        {"dia": 3, "valor": 0.0},    # sem faturamento (feriado ou fim de semana)
        {"dia": 4, "valor": 1500.0},
        {"dia": 5, "valor": 3000.0},
        {"dia": 6, "valor": 0.0},    # sem faturamento (feriado ou fim de semana)
        {"dia": 7, "valor": 1700.0}
    ]
}'''

# Carregar os dados de faturamento do JSON
dados = json.loads(faturamento_diario)

# Filtrar apenas os dias com faturamento
faturamentos = [dia["valor"] for dia in dados["dias"] if dia["valor"] > 0]

# Cálculo do menor, maior faturamento e média
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)

# Contar dias com faturamento superior à média
dias_acima_da_media = len([valor for valor in faturamentos if valor > media_mensal])

# Exibir resultados
print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Média de faturamento: R$ {media_mensal:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
