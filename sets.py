# Declaração de sets

# meu_set = {1, 2, 3, 4}
# print(meu_set)
# print(type(meu_set))
#
# meu_set_2 = set([1, 2, 3, 4])
# print(meu_set_2)

# Operações comuns em sets
meu_set_3 = {1, 2}
# print(meu_set_3)
# meu_set_3.add(3)
# print(meu_set_3)
#
# meu_set_3.update([3, 5, 6])
# print(meu_set_3)
#
#
# meu_set_3.discard(3)
# print(meu_set_3)
#meu_set_3.remove(3)

meu_set_4 = {2, 4}
print(meu_set_3 | meu_set_4)
print(meu_set_3.union(meu_set_4))

print(meu_set_3 & meu_set_4)
print(meu_set_3.intersection(meu_set_4))

print(meu_set_3 - meu_set_4)
print(meu_set_3.difference(meu_set_4))

print(meu_set_3 ^ meu_set_4)
print(meu_set_3.symmetric_difference(meu_set_4))
