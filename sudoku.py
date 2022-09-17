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
        pass

    def resuelto(self):
        pass

    def imprimir_tablero(self):
        pass

class Celda:
    def __init__(self, numero):
        pass

    def insertar(self, numero):
        pass

    def esta_ocupada(self):
        pass

    def get_numero(self):
        pass

    def __str__(self):
        pass


class Conjunto:
    def __init__(self):
        pass

    def insertar(self, numero):
        pass
    
    def contiene(self, numero):
        pass

    def __str__(self):
        pass


class Fila(Conjunto):
    def __init__(self):
        super().__init__()

class Columna(Conjunto):
    def __init__(self):
        super().__init__()

class Cuadrante(Conjunto):
    def __init__(self):
        super().__init__()