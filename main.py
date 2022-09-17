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

    # Agregar codigo para que se juegue la partida

if __name__ == '__main__':
    main()