#tupla = ("a", "b", "c")
#tupla
#('a', 'b', 'c')

#tupla = 100, 200, 300
#tupla
#(100, 200, 300)

#print(tupla)
L = [5, 10, 13, 15, 21, 36, 44, 52, 65, 89]

for x, e in enumerate(L):
    print("%d : %d = %f" % (x, e, x/e))
    
for x, e in enumerate(L):
    print("%d x %d = %i" % (x, e, x * e))
    
for x, e in enumerate(L):
    print("%d + %d = %i" % (x, e, x+e))
    
for x, e in enumerate(L):
    print("%d - %d = %i" % (x, e, x-e))