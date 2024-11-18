import os

# Tabuleiro e estado do jogo como variáveis globais
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
jogador_atual = 'X'

# limpar a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_tabuleiro():
    print("  1   2   3")
    for i in range(3):
        print(f"{i + 1} ", end="")
        for j in range(3):
            print(tabuleiro[i][j], end=" ")
            if j < 2:
                print("| ", end="")
        print()
        if i < 2:
            print("-------------")

def fazer_jogada(linha, coluna):
    if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador_atual
        return True
    return False

def verificar_vencedor():
    # Verificar linhas e colunas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
            return True
    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return True
    return False

def verificar_empate():
    for linha in tabuleiro:
        if ' ' in linha:
            return False
    return True

def trocar_jogador():
    global jogador_atual
    jogador_atual = 'O' if jogador_atual == 'X' else 'X'

def obter_entrada(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, insira um número válido.")

def iniciar_jogo():
    while True:
        limpar_tela()
        print("Tabuleiro atual:")
        exibir_tabuleiro()

        linha = obter_entrada("Digite o número da linha (1, 2 ou 3): ") - 1
        coluna = obter_entrada("Digite o número da coluna (1, 2 ou 3): ") - 1

        if fazer_jogada(linha, coluna):
            if verificar_vencedor():
                limpar_tela()
                exibir_tabuleiro()
                print(f"Jogador {jogador_atual} venceu!")
                break
            elif verificar_empate():
                limpar_tela()
                exibir_tabuleiro()
                print("Empate!")
                break
            trocar_jogador()
        else:
            print("Tente novamente.")
iniciar_jogo()
