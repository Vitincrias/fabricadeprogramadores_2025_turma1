import types

def diz_o_tipo(a):
  tipo = type(a)
  if tipo == str:
    return("String")
  elif tipo == list:
    return("Lista")
  elif tipo == dict:
    return("Dicionário")
  elif tipo == int:
    return("Número inteiro")
  elif tipo == float:
    return("Número decimal")
  elif tipo == types.FunctionType:
    return("Função")
  elif tipo == types.BuiltinFunctionType:
    return("Função interna")
  else:
    return(str(tipo))
  
print(diz_o_tipo("Alô"))
print(diz_o_tipo([2, 3, 4]))
print(diz_o_tipo({
    "nome": "Vitor",
    "idade": 15,
    "cidade": "Sp"
}))
print(diz_o_tipo(1))
print(diz_o_tipo(1.000))
print(diz_o_tipo(lambda argumentos: expressão))
print(diz_o_tipo(len))
print(diz_o_tipo(((1,2))))