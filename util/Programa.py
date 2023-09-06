
class Programa():
    def __init__(self, arquivo):
        self.texto = None
        self.arquivo = arquivo
        self.tabuleiro = []

    def lerArquivoPrograma(self):
        with open(self.arquivo, 'r') as arq:
            self.arquivo = arq
            for linha in self.arquivo:
                # Divida a linha em elementos usando espaços como delimitador
                elementos = linha.split()
                # Converta os elementos em números inteiros (ou float, dependendo dos dados)
                linha_numeros = [int(elemento) for elemento in elementos]
                # Adicione a linha de números à matriz
                self.tabuleiro.append(linha_numeros)
        return self



    def __str__(self):
        matriz_formatada = ""
        for linha in self.tabuleiro:
            linha_formatada = "| "
            for elemento in linha:
                linha_formatada += str(elemento) + " "
            linha_formatada += "|"
            matriz_formatada += linha_formatada + "\n"
        return matriz_formatada