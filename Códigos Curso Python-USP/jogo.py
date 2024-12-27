def main():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    escolha = int(input('''
1 - para jogar uma partida isolada
2 - para jogar um campeonato >>> '''))
    
    if escolha == 1:
        print('\nVocê escolheu uma partida isolada.')
        partida()
    elif escolha <=0 or escolha>2:
        print('\n Você escolheu uma opção invalida, tente novamente.')
        main()
    else:
        print('\nVocê escolheu um campeonato.')
        campeonato()


def computador_escolhe_jogada(n, m):
    if m >= n:
        peças_removidas = n
    else:
        peças_removidas = n % (m + 1)
        if peças_removidas <= 0:
            peças_removidas = m

    print(f'\nO computador tirou {peças_removidas} peça(s).')
    
    return peças_removidas


def usuario_escolhe_jogada(n, m):
    peças_removidas = int(input('\nQuantas peças você vai tirar? '))

    while True:
        if peças_removidas >= 1 and peças_removidas <=min(n,m):
            break
        print('\nJogada inválida! Tente de novo.')
        peças_removidas = int(input('\nQuantas peças você vai tirar? '))

    return peças_removidas


def partida(peças_removidas=0):
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    usuario, computador = False, False

    if (n % (m + 1) == 0):
        print('\nVocê começa!')
        usuario = True
        
    elif n<m or n<=0 or m<=0:

        print("Oops!Inválido,vamos tentar de novo de novo!")
        partida()
        
    else:
        print('\nComputador começa!')
        computador = True

    while usuario:
        peças_removidas = usuario_escolhe_jogada(n, m)
        n -= peças_removidas
        print(f'Agoram resta(m) {n} peça(s) no tabuleiro.')

        peças_removidas = computador_escolhe_jogada(n, m)
        n -= peças_removidas
        if (n == 0):
            break
        print(f'Agoram resta(m) {n} peça(s) no tabuleiro.')

    while computador:
        peças_removidas = computador_escolhe_jogada(n, m)
        n -= peças_removidas
        if (n == 0):
            break
        print(f'Agoram resta(m) {n} peça(s) no tabuleiro.')

        peças_removidas = usuario_escolhe_jogada(n, m)
        n -= peças_removidas
        print(f'Agoram resta(m) {n} peça(s) no tabuleiro.')
    
    print('Fim do jogo! O computador ganhou!')


def campeonato():
    for i in range(1, 4):
        print('\n','*' * 10, f'Rodada {i}', '*' * 10, '\n')
        partida()

    print('\n', '*' * 10, 'Final do campeonato!', '*' * 10)
    print(' ' * 6, 'Placar: Você 0 X 3 Computador')



main()
