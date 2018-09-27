# Declaração

meu_dicionario = {'nome': 'Pedro', 'sobrenome': 'José'}
print(meu_dicionario)
meu_dicionario_2 = dict({1: 'Maria', 2: 'Ana'})
print(meu_dicionario_2)

#Acessando elementos
print(meu_dicionario_2[1])

# Operações sobre dictionaries: get(), len(), del(), pop(), clear()
print(meu_dicionario.get('nome'))

print(len(meu_dicionario))
print(meu_dicionario.pop('nome'))
print(meu_dicionario)

meu_dicionario_3 = dict({1: 'Maria', 2: 'Ana'})
print(meu_dicionario_3)
meu_dicionario_3.clear()
print(meu_dicionario_3)

# meu_dicionario_4 = meu_dicionario_2.copy()
# meu_dicionario_2.pop(2)
# print(meu_dicionario_2)
# print(meu_dicionario_4)

meu_dicionario_4 = meu_dicionario_2
meu_dicionario_2.pop(2)
print(meu_dicionario_2)
print(meu_dicionario_4)

print(meu_dicionario.keys())