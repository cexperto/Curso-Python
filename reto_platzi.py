import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('elige un numero del e al 100'))
    while(numero_elegido!=numero_aleatorio):
        if numero_elegido<numero_aleatorio:
            print('Busque un numero mas grande')
        if numero_elegido>numero_aleatorio:
            print('Busque un numero mas pequeño')
        numero_elegido = int(input('elige un numero del e al 100: '))       
    print("ganaste "+str(numero_elegido)+"maquina "+str(numero_aleatorio))
    
if __name__ == '__main__':
    run()