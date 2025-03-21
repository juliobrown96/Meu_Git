def inverter_string(s):
    invertida = ""
    for i in s:
        invertida = i + invertida
    return invertida

# Testando a função com entrada do usuário
entrada = input("Digite uma string para inverter: ")
print("String invertida:", inverter_string(entrada))
