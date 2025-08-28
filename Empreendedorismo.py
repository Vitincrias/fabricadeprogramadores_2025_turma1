estoque={   "Felca": [ 1000, 2.30],
            "Labubu": [ 500, 0.45],
			"Morango do amor": [ 2001, 1.20],
			"Morango do amor (pistache)": [ 100, 11.99],
            "Boobie goodies": [ 100, 15.99],
            "carlinhos Maia": [ 1, 1.000,50],
            "Virginia": [ 1, 1.9999,99],
            "Morango do amor (Chocolate)": [ 10, 12.99],
            "Morango do amor (Maracuja)": [ 10, 12.99],
            "Morango do amor (açai)": [ 10, 10.00],
            "Canetas tik tok shop": [ 10, 99.99],
            "Labubu (preto)": [ 10, 122.00],
            "Mandioca": [ 10, 2.99],
            "Macaxeira": [ 10, 3.99],
            "Pistache": [ 10, 16.50],
            "Açai de boobie goodies": [ 10, 19.90],
            "Boobie goodies (brain hots)": [ 10, 17.90],
            "Pimentão do amor": [ 10, 8.00],
            "Labubu de boobie goodies, com morango do amor de pistache": [ 10, 199.99],
            "Morango do ódio": [ 19, 7.99]}

kl = input("Digite oque você quer comprar: ")
venda = [ [kl, 
           int(input("Digite o quantidade: "))]]

total = 0
print("Vendas:\n")

if kl in estoque:
    for operação in venda:
        produto, quantidade = operação 
        preço = estoque[produto][1] 
        custo = preço * quantidade
        print("%12s: %3d x %6.2f = %6.2f" %
		    (produto, quantidade,preço,custo))
        estoque[produto][0] -= quantidade 
        total+=custo
else:
    print("Não tem cara, vaza daqui!")
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])