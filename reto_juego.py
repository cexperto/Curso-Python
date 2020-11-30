import random

def imp(valor):
    maquina = random.randint(1,100)
    if valor>maquina:
        print('es menor')
        return valor
    elif valor<maquina:
        print('es mayor')
        return valor
    elif valor==maquina:
        valor=1
        print('Numeros iguales')
        return valor

              
def run():
    valor = 0
    while(True):
        if valor==1:
            print('Gano, finalizo')
            break

        valor = int(input('ingrese numero'))
        valor = imp(valor)


if __name__ == '__main__':
    run()