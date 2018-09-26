# len() para obter o tamanho, append, insert, remove, index, count, sort

#Criando uma lista

lista_simples_inteiro = [1, 2, 3, 4]
lista_simples_string = ["Olá", "Mundo"]
lista_simples_mesclada = [1, 2, 3, "Olá mundo"]
nested_list = [[1, 2], ["Ola", "Mundo"]]

print(nested_list[1][1])

#len()
print(len(lista_simples_inteiro))

#append()
lista_simples_inteiro.append(5)
print(lista_simples_inteiro)

#insert()
lista_simples_inteiro.insert(2, 6)
print(lista_simples_inteiro)

#remove()
lista_simples_inteiro.remove(2)
print(lista_simples_inteiro)

#index()
index = lista_simples_inteiro.index(4)
print(index)

#count()
count = lista_simples_inteiro.count(3)
print(count)

#sort()
lista_simples_inteiro.sort(reverse=False)
print(lista_simples_inteiro)