import json

# Carregar os dados de faturamento de um arquivo JSON
with open('faturamento_diario.json', 'r') as f:
    dados = json.load(f)

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
