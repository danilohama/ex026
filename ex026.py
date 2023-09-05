""""
faça um programa que leia uma frase teclado e mostre:
> quantas vezes aparece a letra "A"
> em que posição ela aparece a primeira vez
> em que posição ela aparece ùltima vez
"""
frase = str(input('Digite uma frase: ')).upper().strip()  # Strip = tira os espaços indesejados
print('A letra "A" aparece {} vezes na frase '.format(frase.lower().count('a')))  # count = conta
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))  # find = encontrar
print('A ultima letra A apareceu na posição {}'.format(
    frase.rfind('A') + 1))  # rfind retorna o índice mais alto da substring se encontrado na string fornecida
