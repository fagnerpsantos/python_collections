from collections import deque

minha_fila = deque(["João", "Pedro", "Augusto"])
minha_fila.append("José")
print(minha_fila)

minha_fila.popleft()
print(minha_fila)