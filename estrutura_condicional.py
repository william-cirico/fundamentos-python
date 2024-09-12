# Estrutura condicional simples
if 10 > 9:
    print("O número 10 é maior que 9")

# Estrutura condicional composta
if 10 > 9:
    print("O número 10 é maior que 9")
elif 10 < 9:
    print("O número 10 é menor que 9")
else:
    print("Os números são iguais")

# Switch
dia_semana = 1

match dia_semana:
    case 1:
        print("Segunda-Feira")
    case 2:
        print("Terça-Feira")
    case 3:
        print("Quarta-Feira")
    case 4:
        print("Quinta-Feira")
    case 5:
        print("Sexta-Feira")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")