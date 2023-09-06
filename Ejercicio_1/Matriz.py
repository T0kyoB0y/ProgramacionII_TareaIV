

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

    def sumar(self, otra):
            temp1 = []
            for i in range(0, self.filas):
                temp2 = []
                for j in range(0, self.columnas):
                    temp2.append((self.matriz[i][j] + otra.matriz[i][j]))
                temp1.append(temp2)
            return temp1
    
    def restar(self, otra):
            temp1 = []
            for i in range(0, self.filas):
                temp2 = []
                for j in range(0, self.columnas):
                    temp2.append((self.matriz[i][j] - otra.matriz[i][j]))
                temp1.append(temp2)
            return temp1
            
    def multiplicar(self, otra):
        nueva_matriz = []




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
    print("Resultado de la suma:")
    suma = matriz1.restar(matriz2)

    print(suma, end="")

    #resta = matriz1.restar(matriz2)
    #print("Resultado de la resta:")
    #resta.imprimir()
    #multiplicacion = matriz1.multiplicar(matriz2)
    #print("Resultado de la multiplicación:")
    #multiplicacion.imprimir()
