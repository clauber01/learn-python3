data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, 
    "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, 
    "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, 
    "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, 
    "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, 
    "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, 
    "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, 
    "87-430": 40
}
age = 16
#your code goes here

# Você está analisando dados de vendas de uma bilheteria.
# O bilhete para um adulto custa $ 20, enquanto o bilhete
# para uma criança com menos de 18 anos custa $ 5. Os dados
# fornecidos estão em formato de dicionário, onde as chaves
# são os números dos ingressos vendidos e os valores são as
# idades do cliente.

# Por exemplo, "123-08": 24 significa que o bilhete foi 
# comprado por um jovem de 24 anos. Seu objetivo é calcular 
# quanto dinheiro a mais o escritório ganharia se mudasse a 
# idade do desconto do ingresso para a entrada fornecida.

# tasck
# Seu objetivo é calcular quanto dinheiro a mais o escritório
# ganharia se mudasse a idade do desconto do ingresso para a 
# entrada fornecida.

# Por exemplo, se o escritório ganhou $ 15.000 com a idade de
# desconto original e ganharia $ 18.000 com 14 como idade de 
# desconto, então o crescimento seria ((18.000-15.000) / 15.000) * 100 = 20%

# Portanto, para a entrada 14, seu programa deve produzir 20.
# A saída deve ser um inteiro (use int () para converter o resultado).

# chaves são os números dos ingressos vendidos
# valores são as idades do cliente.

# print(data.keys())

# idade = input()

def calcular(age, data):
    ganho = 0
    for x in data.values():
        if x < age:
            # print(x)
            ganho += 5
        else:
            ganho += 20
    return ganho

# print(calcular(18, data))
# ganharia = 0
# for y in data.values():
#         # print(y)
#         if y <= age:
#             print(y)
#             ganharia += 5
#         else:
#             ganharia += 20
# print(ganharia)

ganha = calcular(18, data)
ganharia = calcular(age, data)


crescimento = ((ganharia - ganha)/ganha)*100
print(int(crescimento))