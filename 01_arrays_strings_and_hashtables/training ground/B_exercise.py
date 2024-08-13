import sys

input = sys.stdin.read
data = input().split()

text = data[0]  # Número de elementos

word = 'hello'
idx = 0

for character in text:
    if character == word[idx]:
        idx+=1
    if idx == 5:
        break
    
if idx == 5:
    print('YES')
else:
    print('NO')