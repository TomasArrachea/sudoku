from sudoku import Sudoku

def main():
    # leer de un archivo el sudoku y cargarlo en la clase Sudoku
    file = open("tablero.txt", "r")
    tablero = []
    for line in file.readlines():
        tablero.append(line.strip())
    sudoku = Sudoku(tablero)

    print('Tablero inicial:')
    sudoku.imprimir_tablero()

    while not sudoku.resuelto():
        fila = int(input('Ingrese fila: '))
        columna = int(input('Ingrese columna: '))
        numero = int(input('Ingrese numero: '))
        print()
        sudoku.insertar_numero(fila, columna, numero)
        sudoku.imprimir_tablero()

if __name__ == '__main__':
    main()