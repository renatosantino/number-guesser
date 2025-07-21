import random
import os

def limpar_terminal():
    # limpa o terminal para resetar o jogo
    os.system('cls' if os.name == 'nt' else 'clear')    

    
def validar_numero(palpite):
    # checa se o valor digitado é um número inteiro e se está entre 0 e 100. Retorna False se alguma das condições não for satisfeita
    try:
        numero_int = int(palpite)
    except ValueError:
        return False
    
    return 0 <= numero_int <= 100
    

def jogar():
    continuar = 's'

    while continuar == 's':

        # loop que inicia o jogo, gera um número aleatório e zera o contador de tentativas

        numero_random = random.randint(0,100)
        tentativas = 0
        print('Novo número selecionado!')
        print()

        
        while True:

            
            while True:

                # loop vai testar se o palpite do usuário é válido e adicionar uma tentativa ao contador

                palpite_usuario = input('Digite um número de 0 a 100: ')
                if validar_numero(palpite_usuario):
                    palpite_int = int(palpite_usuario)
                    tentativas += 1
                    break
                else:
                    print('Número inválido')

            # esse loop compara o palpite com o número aleatório e retorna se o valor é igual, maior ou menor

            if numero_random == palpite_int:
                print(f'Você acertou! Você precisou de {tentativas} {'tentativas' if tentativas > 1 else 'tentativa'}')

                while True:

                    # loop que oferece ao usuário a opção de reiniciar ou sair do jogo

                    continuar = input('Deseja jogar de novo? [S/N]: ').lower()
                    if continuar and continuar[0] == 's':
                        limpar_terminal()
                        break
                    elif continuar and continuar[0] == 'n':
                        print('Obrigado por jogar!')
                        break
                    else:
                        print('Comando inválido')
                    
                break
            elif numero_random > palpite_int:
                print(f'O número é maior que {palpite_int}')

            elif numero_random < palpite_int:
                print(f'O número é menor que {palpite_int}')

if __name__ == '__main__':
    jogar()
