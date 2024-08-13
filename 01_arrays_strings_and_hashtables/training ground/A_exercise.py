import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])  # Número de elementos
A = list(map(int, data[1:N+1]))  # Elementos del array
X = int(data[N+1])  # Valor a buscar

result = -1

for idx, element in enumerate(A):
    if element == X:
        result = idx
        break

print(result)