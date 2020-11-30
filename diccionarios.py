# objeto = [1,23,45,tr,yu,76]
# objeto.append(1)#agrega un elemento al final de la lista
# objeto.pop()#elimino elemnots por indice
# for elements in objeto:
#     print(elements)
#diccionario=>estructura de datos de llaves y valores
def run():
    mi_diccionario ={
        'llave':1,
        'llave2':2,
        'llave3':3
    }
  #  print(mi_diccionario['llave'])

    # for llave in mi_diccionario.keys():
    #     print(llave)
    for llave in mi_diccionario.values():
        print(llave)
    for llave, valor in mi_diccionario.items():
        print(llave+' tiene '+str(valor)+' cosas')
if __name__=='__main__':
    run()