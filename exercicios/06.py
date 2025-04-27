# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

opcao = input("Agua mineral natural [1] / Agua com gás [2]: ")

preco = 0
if opcao == "1":
    preco = 1.5
    
elif opcao == "2":
    preco = 2.5
    
else:
    print("Entre com o valor correto")
    
print("Valor: R$", preco)