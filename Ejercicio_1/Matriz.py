

class Matriz:

    def __init__(self, filas, columnas, aleatoria=False):
        self.filas = filas
        self.columnas = columnas
        self.aleatoria = aleatoria
        self.matriz = []
        
        if aleatoria:
            temp1 = []
            for i in range(0, self.filas):
                temp2 = []
                for j in range(0, self.columnas):
                    
                    temp2.append(random.randint(0, 9))
                temp1.append(temp2)            
            self.matriz = temp1

        else:
            temp1 = []
            for i in range(0, self.filas):
                temp2 = []
                for j in range(0, self.columnas):
                    
                    temp2.append(0)
                temp1.append(temp2)            
            self.matriz = temp1
            
    def imprimir(self):
        for i in range(len(self.matriz)):
            temp = self.matriz[i]
            print(f"{temp}", end="")

            print("")

    def sumar(self,otra):
        nueva_matriz = []
        if self.filas == otra.filas and self.columnas == otra.columnas:
            for fila in range(0,self.filas):
                for columna in range(0,self.columnas):
                    suma_elemento =  self.matriz[fila][columna] + otra[fila][columna]
                    nueva_matriz[fila][columna] = suma_elemento

        return nueva_matriz
    
    def restar(self,otra):
        nueva_matriz = []
        if self.filas == otra.filas and self.columnas == otra.columnas:
            for fila in range(0,self.filas):
                for columna in range(0,self.columnas):
                    resta_elemento =  self.matriz[fila][columna] + self.otra[fila][columna]
                    nueva_matriz[fila][columna] = resta_elemento

        return nueva_matriz
    def multiplicar(self, otra) :
        nueva_matriz = []
        if self.filas == otra.filas and self.columnas == self.otra.columnas:
            for fila in range(0,self.filas):
                for columna in range(0,self.columnas):
                    continue



import random
if __name__ == "__main__":

    random.seed(7)
    matriz1 = Matriz(5, 5, True)
    random.seed(8)
    matriz2 = Matriz(5, 5, True)
    print("Matriz 1:")
    matriz1.imprimir()
    print("Matriz 2:")
    matriz2.imprimir()
    suma = matriz1.sumar(matriz2)
    print("Resultado de la suma:")
    suma.imprimir()
    #resta = matriz1.restar(matriz2)
    #print("Resultado de la resta:")
    #resta.imprimir()
    #multiplicacion = matriz1.multiplicar(matriz2)
    #print("Resultado de la multiplicación:")
    #multiplicacion.imprimir()
