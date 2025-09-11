import os
print (os.getcwd())

#os.mkdir("d")
#os.mkdir("e")
#os.mkdir("f")

def plmds():
    arquivo_path = ""
    try:
        os.rmdir(arquivo_path)
        print(f"""\033[0;32m Pasta '{arquivo_path}'
            removida com sucesso! ;D""")
    except FileNotFoundError:
        print(f"""\033[0;33m Pasta '{arquivo_path}'
    não encontrada... @@""")
    except OSError:
        print(f"""\033[0;34m '{arquivo_path}'
    é um arquivo, não uma pasta!!! + +""")



Instagram = "50_arquivos"
if not os.path.exists(Instagram):
    os.makedirs(Instagram)

for i in range(1, 51):
    nome_arquivo = f"pasta_{i:03d}.txt"
    facebook = os.path.join(Instagram, nome_arquivo)
    try:
        with open(facebook, "w") as f:
            f.write(f"Vitão bigode \n")
        print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
    except IOError as e:
        print(f"Erro ao criar o arquivo '{nome_arquivo}': {e}")
    print("Criação de arquivos concluída.")
    
try:
    for n in range(1,51):
        os.mkdir("pasta_%d" % n)
        
    os.chdir("pasta_1")
    arquivo = open("arquivo_1.txt", "w")
    arquivo.write("Oi")
    arquivo.close()
except FileNotFoundError:
    print('Arquivo não encontrado!')