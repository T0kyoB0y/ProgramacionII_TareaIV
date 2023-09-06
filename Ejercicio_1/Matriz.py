

class Matriz:

    def __init__(self, filas, columnas, aleatoria=False):
        self.filas = filas
        self.columnas = columnas
        self.aleatoria = aleatoria
        self.matriz = []


    def 
    def imprimir(self):
        for fila in range(0,self.filas):
            for columna in range(0,self.columnas):
                print("fila: ", fila)
                print("columna: ", columna)

    def sumar(self,otra):
        nueva_matriz = []
        if self.filas == otra.filas and self.columnas == otra.columnas:
            for i in range(0,self.filas):
                for k in range(0,self.columnas):
                    nuevo_elemento = i + k
                    print("fila: ", i)
                    print("columna: ", k)


                    

    
    def restar(self,otra):
        print(otra)

    def multiplicar(self, otra) :
        print(otra)


import random
if __name__ == "__main__":

    matriz_1 = Matriz(2,2,True)
    matriz_2 = Matriz(2,2,True)
    #matriz_1.imprimir()
    matriz_1.sumar(matriz_2)


    matriz_x = [[1,2],
        [3,4]
    ]

