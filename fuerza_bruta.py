import string
import getpass

letras = string.ascii_lowercase

# el ejercicio decia que la idea era que se ingrese de manera oculta, pero investigando aprendi que el metodo getpass->
# solo funciona desde terminal, mas no desde el debugger, dejo ambas opciones
code = getpass.getpass('Ingrese la contraseña: ')
# code = input('Ingrese la contraseña: ')
coded = ''
count = 0
while code != coded:
    for pos, letra in enumerate(code):
        for posl, letral in enumerate(letras):
            count += 1
            if letra == letral:
                coded += letral
                break
        if code == coded:
            break
print(f'La contraseña {coded} fue forzada en {count} intentos')
