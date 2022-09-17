class Sudoku:
    def __init__(self, sudoku):
        # sudoku es una lista de strings. Los vacios se representan con 0.        
        # tablero se almacena como matriz de celdas (lista de listas)
        self.tablero = [[None for _ in range(9)] for _ in range(9)] 
        for i, fila in enumerate(sudoku):
            for j, numero in enumerate(fila):
                self.tablero[i][j] = Celda(int(numero))

        # inicializar filas, columnas y cuadrantes
        self.filas = []
        self.columnas = []
        self.cuadrantes = []
        for i in range(9):
            self.filas.append(Fila())
            self.columnas.append(Columna())
            self.cuadrantes.append(Cuadrante())

        for i, fila in enumerate(self.tablero):
            for j, celda in enumerate(fila):
                self.filas[i].insertar(celda.get_numero())
                self.columnas[j].insertar(celda.get_numero())
                self.get_cuadrante(i, j).insertar(celda.get_numero())

    def get_cuadrante(self, fila, columna):
        return self.cuadrantes[(fila//3)*3 + columna//3]

    def insertar_numero(self, fila, columna, numero):
        if self.tablero[fila][columna].esta_ocupada():
            print('La celda ya esta ocupada')

        elif self.filas[fila].contiene(numero):
            print('El numero ya esta en la fila')

        elif self.columnas[columna].contiene(numero):
            print('El numero ya esta en la columna')
        
        elif self.get_cuadrante(fila, columna).contiene(numero):
            print('El numero ya esta en el cuadrante')

        else:
            self.tablero[fila][columna].insertar(numero)
            self.filas[fila].insertar(numero)
            self.columnas[columna].insertar(numero)
            self.get_cuadrante(fila, columna).insertar(numero)
            print('Numero insertado')

    def resuelto(self):
        for fila in self.tablero:
            for celda in fila:
                if celda.esta_ocupada() == False:
                    return False
        return True
        
    def imprimir_tablero(self):
        # opcional, con que imprima el tablero con espacios esta bien
        j = 0
        print(" ----------------------- ")
        for fila in self.tablero:
            i = 0
            if j == 3 or j == 6:
                print("|-----------------------|")
            for celda in fila:
                if i == 0 or i == 3 or i == 6:
                    print("| ", end="")
                print(celda, end=" ")
                i += 1
            print("|")        
            j += 1
        print(" ----------------------- ")


class Celda:
    def __init__(self, numero):
        self.numero = numero

    def insertar(self, numero):
        self.numero = numero

    def esta_ocupada(self):
        return self.numero != 0

    def get_numero(self):
        return self.numero

    def __str__(self):
        return str(self.numero)


class Conjunto:
    def __init__(self):
        self.numeros = set()

    def insertar(self, numero):
        self.numeros.add(numero)
    
    def contiene(self, numero):
        return numero in self.numeros

    def __str__(self):
        return str(self.numeros)


class Fila(Conjunto):
    def __init__(self):
        super().__init__()

class Columna(Conjunto):
    def __init__(self):
        super().__init__()

class Cuadrante(Conjunto):
    def __init__(self):
        super().__init__()