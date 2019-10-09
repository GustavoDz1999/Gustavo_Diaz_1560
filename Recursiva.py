def sumador_arreglo(lista):
    if type(lista)==list:        
        indice=len(lista)
        if indice==0:
            return 0
        else:
            m=lista[indice-1]
            lista.pop()
            return m + sumador_arreglo(lista)
    else:
        return "Debes ingresar una lista"

def main():
  print(sumador_Arreglo(8))
  print(sumador_Arreglo([7,6,5,4,3,2,8]))
