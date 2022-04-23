numero = input('Ingresa tu RUT sin puntos ni dígito verificador: ')
serie = [2, 3, 4, 5, 6, 7]
numrev = list(map(int, numero[::-1]))
conta = 0
suma = 0
while len(serie) != len(numrev):
    serie.append(serie[conta])
    conta += 1
for pos, num in enumerate(numero):
    suma += int(numrev[pos]) * int(serie[pos])
modulo = 11-(suma % 11)
print(f'{(suma % 11)}\nSu dígito verificador es {modulo}')
