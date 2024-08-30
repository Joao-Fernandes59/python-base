"""
Faça um programa que imprime os núneros pares de 1 a 200

Exemplo:
'python numeros.pares.py'
2
4
6
8
...
"""

for num in range(1, 201):
    if num % 2 != 0:
        continue
    print(num)

print("-" * 50)

i = 0
while i < 201:
    i += 1
    if i % 2 != 0:
        continue
    print(i)
