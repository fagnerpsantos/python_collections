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

#Unions, intersections...
meu_set_4 = {2, 4}
print(meu_set_3 | meu_set_4)
print(meu_set_3.union(meu_set_4))

print(meu_set_3 & meu_set_4)
print(meu_set_3.intersection(meu_set_4))

print(meu_set_3 - meu_set_4)
print(meu_set_3.difference(meu_set_4))

print(meu_set_3 ^ meu_set_4)
print(meu_set_3.symmetric_difference(meu_set_4))

#Set Comprehensions
meu_set_5 = {i for i in meu_set_3.union(meu_set_4)}
print(f"Meu set {meu_set_5}")

#Frozen Sets
frozen_set_1 = frozenset([1, 2, 3, 4])
frozen_set_2 = frozenset([1, 2, 5, 6])
print(frozen_set_1)
print(frozen_set_2)
print(frozen_set_1.union(frozen_set_2))
frozen_set_1.add(4)
