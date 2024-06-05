def SOMA (x,y):
    return x + y

def SUBTRAÇÃO (x,y):
    return x - y

def MULTIPLICAÇÃO (x,y):
    return x * y

def DIVISÃO (x,y):
    return x / y

def POTENCIA (x,y):
    return x ** y


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Calculadora<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("1-SOMA")
print("2-SUBTRAÇÃO")
print("3-MULTIPLICAÇÃO")
print("4-DIVISÃO")
print("5-POTENCIA")


opcão = int(input("\nDigite a opcão desejada (1/2/3/4/5/6):"))

if opcão <=0 or opcão > 6:
    print("opcão invalida")
    exit(0)

valor_A = int(input(" Digite o valor A: "))
valor_B = int(input(" Digite o valor B: "))

if opcão == 1:
    print(valor_A, "+",valor_B, "=",
          SOMA(valor_A,valor_B))

if opcão == 2:
    print(valor_A, "-",valor_B, "=",
          SOMA(valor_A,valor_B))

if opcão == 3:
    print(valor_A, "*",valor_B, "=",
          SOMA(valor_A,valor_B))

if opcão == 4:
    print(valor_A, "/",valor_B, "=",
          SOMA(valor_A,valor_B))

if opcão == 5:
    print(valor_A, "**",valor_B, "=",
          SOMA(valor_A,valor_B))

