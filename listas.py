# len() para obter o tamanho, append, insert, remove, index, count, sort

#Criando uma lista

lista_simples_inteiro = [1, 2, 3, 4]
lista_simples_string = ["Olá", "Mundo"]
lista_simples_mesclada = [1, 2, 3, "Olá mundo"]
nested_list = [[1, 2], ["Ola", "Mundo"]]

# print(nested_list[1][1])
#
# #len()
# print(len(lista_simples_inteiro))
#
# #append()
# lista_simples_inteiro.append(5)
# print(lista_simples_inteiro)
#
# #insert()
# lista_simples_inteiro.insert(2, 6)
# print(lista_simples_inteiro)
#
# #remove()
# lista_simples_inteiro.remove(2)
# print(lista_simples_inteiro)
#
# #index()
# index = lista_simples_inteiro.index(4)
# print(index)
#
# #count()
# count = lista_simples_inteiro.count(3)
# print(count)
#
# #sort()
# lista_simples_inteiro.sort(reverse=False)
# print(lista_simples_inteiro)

# Copiando listas

# Shallow Copy
# nova_lista_inteiro = lista_simples_inteiro
# print(lista_simples_inteiro)
# lista_simples_inteiro.append(8)
# print(lista_simples_inteiro)
# print(nova_lista_inteiro)
#
# nova_lista_inteiro_1 = lista_simples_inteiro.copy()
# lista_simples_inteiro.append(9)
# print(lista_simples_inteiro)
# print(nova_lista_inteiro_1)

# List comprehensions
# nova_lista = []
# for i in lista_simples_inteiro:
#     nova_lista.append(i * i)
# print(nova_lista)
#
# nova_lista_elegante = [i * i for i in lista_simples_inteiro]
# print(nova_lista_elegante)

# Slices

lista_simples_inteiro_2 = [1, 2, 3, 4]
print(lista_simples_inteiro_2[1:3])
print(lista_simples_inteiro_2[2:])
nova_lista = lista_simples_inteiro_2[2:]
print(nova_lista)
