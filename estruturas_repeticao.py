# For simples
for i in range(10):
    print(i)

for i in range(1, 10, 2):
    print(i)

# Lista
frutas = ["🍎", "🍇", "🍉"]

for fruta in frutas:
    print(fruta)

while True:
    numero = int(input("Digite um número par: "))

    if numero % 2 == 0:
        break