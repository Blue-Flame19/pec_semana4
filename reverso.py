numero = int(input(""))
numero_revs = 0

while (numero>0):
    sobra = numero%10
    numero_revs = (numero_revs*10) + sobra
    numero = numero//10

print(numero_revs)
