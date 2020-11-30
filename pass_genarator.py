import random

def passGenerate():
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    simbolos = ['!','#','$','%','&','/','(',')','=','?','¡','¿','*','+','-']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    characteres = mayusculas + minusculas + simbolos + numeros
    myPass = []
    for i in range(15):
        character_random= random.choice(characteres)
        myPass.append(character_random)
    passList = ''.join(myPass)
    return passList


def run():
    password = passGenerate()
    print('tu contrasena es '+password)


if __name__ =='__main__':
    run()