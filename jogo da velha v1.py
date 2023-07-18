import random
import time

print('───'*6,end=' ')
print(' ')
print('JOGO DA VELHA V.1',end=' ')
print(' ')
print('───'*6,end=' ')
print(' ')
print('SEGUE O MODELO DE TABULEIRO UTILIZADO:')


print("\n")
print('│ 0 │ 1 │ 2 │')
print("├───┼───┼───┤")
print(f"│ 3 │ 4 │ 5 │")
print("├───┼───┼───┤")
print(f"│ 6 │ 7 │ 8 │")
print("\n")
print('──'*8,end=' ')
print(' ')
time.sleep(2)

while True:

    jogo = (input('deseja jogar contra a maquina?'))
    if jogo == 'S' or jogo == 's' or jogo == 'sim' or jogo == '1':
        modo = 1
        break
    elif jogo == 'N' or jogo == 'n' or jogo == 'nao':
        modo = 0
        break
    else :
         print('Nenhum modo de jogo foi selecionado, tente novamente.')


def imprimir_tabuleiro(tabuleiro):
    print("\n")
    print(f"│ {tabuleiro[0]} │ {tabuleiro[1]} │ {tabuleiro[2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro[3]} │ {tabuleiro[4]} │ {tabuleiro[5]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro[6]} │ {tabuleiro[7]} │ {tabuleiro[8]} │")
    print("\n")

# Função para verificar se um jogador ganhou
def verificar_vencedor(tabuleiro, jogador):
    if (tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador) or \
       (tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador) or \
       (tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador) or \
       (tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador) or \
       (tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador) or \
       (tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador) or \
       (tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador) or \
       (tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador):
        return True
    else:
        return False

# Função para realizar a jogada da máquina
def jogada_maquina(tabuleiro, jogador, maquina):
    # Realiza uma jogada aleatória
    while True:
        print('o computador esta pensando...')
        time.sleep(1)
        posicao = random.randint(1, 9)
        if tabuleiro[posicao] == ' ':
            return posicao

# Função principal do jogo
def jogar_jogo_da_velha():
    tabuleiro = [' '] * 9
    jogador = 'X'
    maquina = 'O'
    turno = 'jogador'


    if modo == 1 : #modo de jogo contra a maquina
        while True:
            imprimir_tabuleiro(tabuleiro)

            if turno == 'jogador':
                posicao = int(input("Sua vez, digite a posição para jogar(0-8):"))
                if tabuleiro[posicao] == ' ':
                    tabuleiro[posicao] = jogador
                    if verificar_vencedor(tabuleiro, jogador):
                        imprimir_tabuleiro(tabuleiro)
                        print("Parabéns! Você venceu!")
                        break
                    turno = 'maquina'
                else:
                    print("Posição inválida. Tente novamente.")

            elif turno == 'maquina':
                posicao = jogada_maquina(tabuleiro, jogador, maquina)
                tabuleiro[posicao] = maquina
                if verificar_vencedor(tabuleiro, maquina):
                    imprimir_tabuleiro(tabuleiro)
                    print("Você perdeu! A máquina venceu.")
                    break
                turno = 'jogador'

            if ' ' not in tabuleiro:
                imprimir_tabuleiro(tabuleiro)
                print("Empate!")
                break

    if modo == 0: # modo de jogo com dois jogadores
        while True:
            imprimir_tabuleiro(tabuleiro)
            posicao = int(input('Digite a posição(0-8): '))

            if tabuleiro[posicao] == ' ':
                tabuleiro[posicao] = jogador
                if verificar_vencedor(tabuleiro,maquina):
                    imprimir_tabuleiro(tabuleiro)
                    print('O jogador', jogador, 'venceu!')
                    break
                elif ' ' not in tabuleiro:
                    imprimir_tabuleiro(tabuleiro)
                    print('O jogo empatou!')
                    break
                elif jogador == 'X':
                    jogador = 'O'
                else:
                    jogador = 'X'

            else:
                print('Movimento inválido. Tente novamente.')

# Iniciar o jogo
jogar_jogo_da_velha()

