#punto de entrada
def palindromo(palabraPalindromo):
    palabraPalindromo = palabraPalindromo.replace(' ','').lower()
    if palabraPalindromo == palabraPalindromo[::-1]:
        return True
    else:
        return False

def run():
    palabra = input(str("introduzca la palabra: "))
    esPalindromo = palindromo(palabra)
    if esPalindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()
    run2()

