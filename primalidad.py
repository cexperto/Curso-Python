def esPrimo(numero):
    contador = 0
    for i in range(2,numero+1):
        if i ==1 or i == numero:
            continue
        if numero %1 ==0:
            contador =+1
    if contador ==0:
        return True
    else:
        return False

def run():
    numero = int(input('digite un numero'))
    if esprimo(numero)==True:
        print('es primo')
    else:
        print('No es primo')

if __name__ == '__main__':
    run()
