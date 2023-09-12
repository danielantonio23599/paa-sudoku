import argparse

from util.Programa import Programa
from util.Sudoku import Sudoku
from util.Teste import Teste


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument('filename', help='Arquivo .txt')
parser.add_argument('-head', dest='head', type=str, help='Customiza delimitadores do cabeçote')
args = parser.parse_args()

# ------------------------ Simulador ----------------------------------------
print('Solver de Sudoku ver 1.0 - IFMG 2023')
print('Desenvolvido como trabalho prático para a disciplina de PAA')
print('Autores: Daniel Antônio de Sá')

tabuleiro = Programa(args.filename).lerArquivoPrograma()
sudoku = Sudoku(tabuleiro.tabuleiro, 0, 0)
sudoku.solver()
# teste = Teste(sudoku.tabuleiro)
# teste.validar()
