import json

faturamento_json = '{"faturamento": [{"dia": 1, "valor": 1000}, {"dia": 2, "valor": 2000}, {"dia": 3, "valor": 0}, {"dia": 4, "valor": 3000}, {"dia": 5, "valor": 2500}, {"dia": 6, "valor": 0}, {"dia": 7, "valor": 1800}, {"dia": 8, "valor": 2200}, {"dia": 9, "valor": 0}, {"dia": 10, "valor": 2700}]}'

dados = json.loads(faturamento_json)
faturamento = [d["valor"] for d in dados["faturamento"] if d["valor"] > 0]

print("Menor:", min(faturamento))
print("Maior:", max(faturamento))
print("Dias acima da média:", sum(f > (sum(faturamento) / len(faturamento)) for f in faturamento))