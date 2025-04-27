# %%

numero = 1

while numero <= 100:
    print(numero)
    numero = numero + 1

print("Acabou!")

# %%

soma_notas = 0

while True:
    nota = input("Entre com a nota: ")
    if nota == "":
        break
    soma_notas += float(nota)
    
print(soma_notas)