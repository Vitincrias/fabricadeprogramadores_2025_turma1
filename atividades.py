def quadrado(Lado):
    area = Lado ** 2
    return area
print(quadrado(30))

def reajuste(salario):
    novo = salario + salario * 0.15
    return novo
print(reajuste(1000))

def triangulo(altura,base):
    resultado = (altura * base) /2
    return resultado
print(triangulo(5,3))

def temperatura(celsius):
    resposta =(9*celsius+160) /5
    return resposta
print(temperatura(100))

def equação(Y,X):
    resposta = (X,Y)
    return resposta
print(equação(10,25))