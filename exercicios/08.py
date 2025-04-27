# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50),
# cestinha (R$4,00)
# 
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

tipo = input("Tipo: Casquinha [1] / Cascão [2] / Cestinha [3]: ")
sabor = input("Sabor: Morango [1] / Creme [2] / Chocolate [3]: ")
cobertura = input("Cobertura: Caramelo [1] / Morango [2] / Chocolate [3] / NDA [4]")

preco = 0

if tipo == "1":
    preco = preco + 1
elif tipo == "2":
    preco += 2.5
elif tipo == "3":
    preco += 2.5
else:
    print("Entre com a caralha do preoco certo!")

if cobertura == "1":
    preco += 1.5
elif cobertura == "2":
    preco += 1.5
elif cobertura == "3":
    preco += 1.5
else:
    preco += 0
    
print("Valor total: R$", preco)