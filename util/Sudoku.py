from itertools import chain


class Sudoku:

    def __init__(self, tabuleiro, linha, coluna):
        self.tabuleiro = tabuleiro
        self.linha = linha
        self.coluna = coluna
        self.para = False

    def solver(self):
        if self.tabuleiro[self.linha][self.coluna] == 0:
            # validar linha para prosseguir a linha de busca
            if sum(self.tabuleiro[self.linha]) > 45:
                return
            # validar coluna para processeguir a linha de busca
            if self.soma_coluna(self.tabuleiro, self.coluna) > 45:
                return
            if self.soma_quadrate() > 45:
                return
            # Gere as escolhas possíveis para a próxima etapa
            escolhas = self.gerar_escolhas()

            # Para cada escolha possível
            for escolha in escolhas:
                # Recursivamente, avance para a próxima etapa
                linha = self.linha
                coluna = self.coluna
                self.tabuleiro[linha][coluna] = escolha
                self.linha, self.coluna = self.proximo()
                self.solver()
                if self.para:
                    return self.tabuleiro
                else:
                    # Desfaça a escolha (backtrack) para explorar outras opções
                    self.tabuleiro[linha][coluna] = 0
                    self.coluna = coluna
                    self.linha = linha
        else:
            # Verifique se a solução atual é uma solução válida
            if self.is_valid_sudoku(self.tabuleiro):
                print()
                print(self.__str__())
                self.para = True
                return
            self.linha, self.coluna = self.proximo()
            self.solver()

    def proximo(self):
        if self.coluna < 8:
            self.coluna += 1
        else:
            self.coluna = 0
            if self.linha < 8:
                self.linha += 1
        return self.linha, self.coluna

    # Função para gerar escolhas possíveis para a próxima etapa
    def gerar_escolhas(self):
        existentes = set(self.tabuleiro[self.linha]
                         + self.extrai_coluna(self.tabuleiro, self.coluna)
                         + self.lista_quadrante(self.tabuleiro, self.linha, self.coluna)
                         )
        return list({1, 2, 3, 4, 5, 6, 7, 8, 9} - existentes)

    def extrai_coluna(self, tabuleiro, coluna):
        return [linha[coluna] for linha in tabuleiro]

    def is_valid_sudoku(self, tabuleiro):
        # Verificar linhas e colunas
        if not self.is_valid_linhas(tabuleiro):
            return False
        if not self.is_valid_colunas(tabuleiro):
            return False
        return self.is_valid_quadrante(tabuleiro)

    def is_valid_linhas(self, tabuleiro):
        for linha in tabuleiro:
            if 45 != sum(linha):
                return False
        return True

    def is_valid_colunas(self, tabuleiro):
        for i in range(9):
            if 45 != self.soma_coluna(tabuleiro, i):
                return False
        return True

    def soma_coluna(self, tabuleiro, coluna):
        soma = 0
        for linha in tabuleiro:
            soma += linha[coluna]
        return soma

    def soma_quadrate(self):
        return sum(self.lista_quadrante(self.tabuleiro, self.linha, self.coluna))
    def is_valid_quadrante(self, tabuleiro):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                quadrante = tabuleiro[i:i + 3]
                if sum(sum(row[j:j + 3]) for row in quadrante) != 45:
                    return False
        return True

    def define_quadrante(self, linha, coluna):
        if linha < 3:
            if coluna < 3:
                return 1
            if coluna < 6:
                return 2
            return 3
        if linha < 6:
            if coluna < 3:
                return 4
            if coluna < 6:
                return 5
            return 6
        if coluna < 3:
            return 7
        if coluna < 6:
            return 8
        return 9

    def lista_quadrante(self, tabuleiro, linha, coluna):
        if self.define_quadrante(linha, coluna) == 1:
            return list(set(chain(*(row[0:3] for row in tabuleiro[0:3]))))
        if self.define_quadrante(linha, coluna) == 2:
            return list(set(chain(*(row[3:6] for row in tabuleiro[0:3]))))
        if self.define_quadrante(linha, coluna) == 3:
            return list(set(chain(*(row[6:9] for row in tabuleiro[0:3]))))
        if self.define_quadrante(linha, coluna) == 4:
            return list(set(chain(*(row[0:3] for row in tabuleiro[3:6]))))
        if self.define_quadrante(linha, coluna) == 5:
            return list(set(chain(*(row[3:6] for row in tabuleiro[3:6]))))
        if self.define_quadrante(linha, coluna) == 6:
            return list(set(chain(*(row[6:9] for row in tabuleiro[3:6]))))
        if self.define_quadrante(linha, coluna) == 7:
            return list(set(chain(*(row[0:3] for row in tabuleiro[6:9]))))
        if self.define_quadrante(linha, coluna) == 8:
            return list(set(chain(*(row[3:6] for row in tabuleiro[6:9]))))
        if self.define_quadrante(linha, coluna) == 9:
            return list(set(chain(*(row[6:9] for row in tabuleiro[6:9]))))

    def __str__(self):
        matriz_formatada = ""
        for i in range(9):
            linha = self.tabuleiro[i]
            linha_formatada = " "
            for indice in range(9):
                linha_formatada += str(linha[indice]) + " "
                if indice == 2 or indice == 5:
                    linha_formatada += "| "
            linha_formatada += " "
            matriz_formatada += linha_formatada + "\n"
            if i == 2 or i == 5:
                matriz_formatada += " - - -   - - -   - - -  \n"
        return matriz_formatada