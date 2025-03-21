faturamento = [1000, 2000, 1500, 3000, 2500, 0, 1800, 2200, 0, 2700]

faturamento = [f for f in faturamento if f > 0]

print("Menor faturamento:", min(faturamento))
print("Maior faturamento:", max(faturamento))

media = sum(faturamento) / len(faturamento)
print("Dias acima da média:", sum(1 for f in faturamento if f > media))