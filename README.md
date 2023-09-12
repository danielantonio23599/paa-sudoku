# paa-sudoku
# Título do Projeto: Implementação de um Solver de Sudoku com o paradigma de Força Bruta

# Descrição:

-- Neste projeto de programação, você será desafiado a criar um programa em uma linguagem de programação de sua escolha que seja capaz de resolver automaticamente quebra-cabeças de Sudoku usando o paradigma de Força Bruta. O Sudoku é um jogo de lógica onde o objetivo é preencher uma matriz 9x9 com números de 1 a 9, de modo que cada linha, coluna e submatriz 3x3 contenha todos os números de 1 a 9 sem repetições. -- 

# Tarefas Principais:
-- Desenvolver um programa que permita a entrada de quebra-cabeças de Sudoku incompletos, representados como uma matriz 9x9, onde espaços vazios (células não preenchidas) são indicados pelo número 0.
Implementar um algoritmo para gerar a solução usando o paradigma de Força Bruta (Backtracking OU Branch & Bound). O algoritmo deve ser capaz de encontrar uma solução válida para qualquer quebra-cabeça de Sudoku válido informado como entrada.
Ao ser invocado pela linha de comando, o programa deverá receber um arquivo de texto como entrada (vide anexos/links), representando uma matriz de 9x9 com números de 1 a 9, contendo 9 colunas separadas por ' ' (espaço) e 9 linhas separadas por '\n'
Por segurança, recomendo que garanta que o programa valide a entrada para garantir que ela representa um quebra-cabeça válido de Sudoku (ou seja, a própria entrada não viola as regras do Sudoku).
Ao final, o programa deverá exibir no terminal a solução gerada (vide anexos/links), exibindo-a de preferência no mesmo formato da entrada. Não é necessário exibir o tabuleiro de Sudoku formatado.--
# Requisitos Técnicos:
Use a linguagem de programação de sua escolha.
Deverá ser entregue um RELATÓRIO onde: explicará brevemente o problema abordado; explicará em detalhe sua modelagem do problema para o paradigma utilizado; indicará os pontos fortes e fracos do algoritmo.
O código-fonte deve ser bem organizado, modular e acompanhado de alguns comentários explicativos nos trechos mais relevantes.
Você deve IMPRETERIVELMENTE usar um paradigma de Força Bruta (Backtracking OU Branch & Bound) para encontrar a solução do Sudoku. Não serão aceitas soluções que utilizem outros tipos de paradigmas.
Naturalmente, como irá receber o quebra-cabeça como entrada, seu programa deve ser capaz de lidar com diferentes quebra-cabeças de Sudoku (ex.: fácil, médio e, quem sabe, difícil). Esse é apenas um lembrete para você não colocar o(s) quebra-cabeça(s) "hard coded" em seu programa.
EXEMPLO DE ENTRADA:
0 0 2 0 0 0 5 0 0
0 1 0 7 0 5 0 2 0
4 0 0 0 9 0 0 0 7
0 4 9 0 0 0 7 3 0
8 0 1 0 3 0 4 0 9
0 3 6 0 0 0 2 1 0
2 0 0 0 8 0 0 0 4
0 8 0 9 0 2 0 6 0
0 0 7 0 0 0 8 0 0

EXEMPLO DE SAÍDA (para a entrada acima):
9 7 2 8 6 3 5 4 1
6 1 8 7 4 5 9 2 3
4 5 3 2 9 1 6 8 7
5 4 9 1 2 8 7 3 6
8 2 1 6 3 7 4 5 9
7 3 6 4 5 9 2 1 8
2 9 5 3 8 6 1 7 4
1 8 4 9 7 2 3 6 5
3 6 7 5 1 4 8 9 2

# Mais exemplos de entradas: 
http://lipas.uwasa.fi/~timan/sudoku/sudokus.zip
http://lipas.uwasa.fi/~timan/sudoku/

# solver-sudoku
Solver do jogo de sudoku

Como iniciar o programa:

    python sudoku.py <arquivo>
Exemplo: 
    
    python sudoku.py teste.txt
