def SOS():
    X=1
    while X<=50000:
        print(X)
        X= X+1

def Senhor():
    X=1
    while X<=100:
        print(X)
        X= X+1 


def ola_gostaria():
    X=50
    while X<=100:
        print(X)
        X= X+1

def slk():
    Y = 0
    while Y <= 10:
        print(Y)
        Y = Y+1
    print ("já, Fogo!")

def q_saco():
    fim=int(input("Digite o último número a imprimir: "))
    x=0
    while x <= fim:
        if x % 2 == 0:
            print(x)
        x=x+1

fim=int(input("Digite o último número a imprimir: "))
x=0
while x <= fim:
    if x % 2 == 1:
        print(x)
    x=x+1