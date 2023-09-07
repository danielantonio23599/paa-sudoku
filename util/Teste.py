class Teste:

    def __init__(self, matriz):
        self.matriz = matriz

    def is_valid_sudoku(self, matriz):
        # Verificar cada linha
        for linha in matriz:
            if len(set(linha)) != 9:
                return False

        # Verificar cada coluna
        for coluna in zip(*matriz):
            if len(set(coluna)) != 9:
                return False

        # Verificar cada subgrade 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [matriz[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if len(set(subgrid)) != 9:
                    return False

        return True

    def validar(self):
        if self.is_valid_sudoku(self.matriz):
            print("A matriz é válida para um jogo de Sudoku.")
        else:
            print("A matriz não é válida para um jogo de Sudoku.")
