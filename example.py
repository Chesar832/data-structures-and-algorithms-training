import sys
 
read = sys.stdin.readline # Lee la linea completa, igual que input()
write = sys.stdout.write # Imprime sin salto de linea al final, asi que agregar '\n' cuando lo requieran.
 
t = int(read())

for _ in range(t):
    a, b, n = map(int, read().split())
    a *= n
    b *= n
    if b >= 100:
        a += b // 100
        b %= 100
    write("{:d} {:d}\n".format(a, b))