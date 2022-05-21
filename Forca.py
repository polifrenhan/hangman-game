'''

Olá, esse foi um dos primeiros projetos em Python que desenvolvi.
É um projeto de estudo dos conceitos: If-Else, While, For e Listas,
conteudo das aulas 1 a 11 do curso do Otávio Miranda:
https://www.youtube.com/playlist?list=PLbIBj8vQhvm0ayQsrhEf-7-8JAj-MwmPr

'''
import time
import sys
import random


def delay_print(texto_lento, velocidade):
    for letra in texto_lento:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    print('')


lista_palavras = [
    ['BORBOLETA', 'CAVALO', 'CACHORRO', 'CARANGUEJO', 'CHIMPANZE', 'COELHO', 'JACARE', 'ELEFANTE', 'GALINHA', 'GIRAFA',
     'LEAO', 'GATO', 'SAPO', 'VEADO', 'TIGRE', 'GRILO', 'FORMIGA', 'ABELHA', 'HIPOPOTAMO', 'GOLFINHO', 'TIGRE',
     'CAPIVARA',
     'ESQUILO', 'RATO', 'PORCO'],
    ['BAILARINA', 'PINTOR', 'MIMICO', 'ASTRONAUTA', 'PROFESSOR', 'MEDICO', 'ARTISTA', 'PESCADOR',
     'POLICIAL', 'SURFISTA', 'VENDEDOR', 'CHEFE', 'ATLETA', 'ENGENHEIRO', 'ADVOGADO', 'JUIZ', 'LIXEIRO', 'SECRETARIA',
     'PRESIDENTE',
     'DOMESTICA'],
    ['ESTATUA', 'ESCOVA DE DENTES', 'LAPIS', 'LIVRO', 'CADEIRA', 'SACOLA', 'CALCULADORA', 'SEMENTE', 'BILHETE',
     'CARTEIRA', 'MAQUINA DE LAVAR', 'PRANCHA DE SURFE', 'LIXO', 'CADEADO', 'AVIAO', 'BALAO', 'BOLO', 'CAMA', 'CANECA',
     'CELULAR',
     'COPO', 'ESTOJO', 'FACA', 'FOTO', 'GARFO', 'JANELA', 'MEIA', 'OCULOS', 'ONIBUS', 'PIJAMA']]
categoria_palavras = ['Animal', 'Profissão/Função', 'Coisa/Objeto']
animacao_1 = f'''              ____________
              ||         |
              ||         💀
              ||
              ||
'''
animacao_2 = f'''              ____________
              ||         |
              ||         💀
              ||         |
              ||
'''
animacao_3 = f'''              ____________
              ||         |
              ||         💀
              ||        /|
              ||
'''
animacao_4 = f'''              ____________
              ||         |
              ||         💀
              ||        /|\\
              ||
'''
animacao_5 = f'''              ____________
              ||         |
              ||         💀
              ||        /|\\
              ||        / 
'''
animacao_6 = f'''              ____________
              ||         |
              ||         💀
              ||        /|\\
              ||        / \\ 
'''
animacao_erros = [animacao_1, animacao_2, animacao_3, animacao_4, animacao_5, animacao_6]
animacao_gameover = f'''
{'':💀^25}
{'':💀^25}
{' G A M E O V E R ':💀^31}
{'':💀^25}
{'':💀>25}
'''

print(f'''{'':#^40}
{'':#^40}
{' 🪢 JOGO DA FORCA 🪢 ':#^38}
{'':#^40}
{' by Poli ##':#>40}
''')
delay_print((f'''{'Você já sabe a regra...': ^40}
'''), 0.25)
print(f'''{' NÃO ': ^40}''')
time.sleep(1)
print(animacao_6)
time.sleep(1)
print(f'''{'MORRA!': ^40}
''')
time.sleep(1)
while True:
    start = input('''Pronto para jogar?
(s - sim | outra letra - sair)
Resposta: ''')
    if start.upper() == 'S':
        lista_escolhida = lista_palavras[random.randrange(len(lista_palavras))]
        palavra = lista_escolhida[random.randrange(len(lista_escolhida))]

        tamanho_palavra = 0
        contador_espaco = 0
        categoria = 0
        erro = 0
        palavra_sem_espaco = ''
        animacao_palavra = ''
        espaco = ' '

        if espaco in palavra:
            for letra in palavra:
                if letra == espaco:
                    contador_espaco += 1
                    animacao_palavra += espaco
                else:
                    palavra_sem_espaco += letra
                    animacao_palavra += '_'
            tamanho_palavra = len(palavra_sem_espaco)
        else:
            tamanho_palavra = len(palavra)
            animacao_palavra = '_' * tamanho_palavra

        index_nomes = 0
        if lista_escolhida == lista_palavras[1]:
            index_nomes = 1
        elif lista_escolhida == lista_palavras[2]:
            index_nomes = 2
        print(
            f'Palavra sorteada... Categoria: {categoria_palavras[index_nomes]}. Número de palavras: {contador_espaco + 1}. Total de letras: {tamanho_palavra}.')
        delay_print(animacao_palavra, 0.25)
        palavra_recebida = ''
        while palavra_recebida != palavra:
            letra_digitada = (input('Digite uma letra: ')).upper()
            if len(letra_digitada) > 1:
                print('Digite apenas uma letra!')
                continue
            palavra_oculta = ''
            if letra_digitada in palavra:
                palavra_recebida += letra_digitada
                for letra_oculta in palavra:
                    if letra_oculta == espaco:
                        palavra_oculta += espaco
                    elif letra_oculta in palavra_recebida:
                        palavra_oculta += letra_oculta
                    else:
                        palavra_oculta += '_'
                palavra_recebida = palavra_oculta
                print(palavra_oculta)
            else:
                if erro < 5:
                    print(f'''

LETRA INCORRETA!
{animacao_erros[erro]}
{5 - erro} chances restantes

''')
                    erro += 1
                else:
                    print(animacao_6)
                    delay_print(animacao_gameover, 0.05)
                    break
        if palavra_recebida == palavra:
            print(f'''
Muito bem, vamos ver até quando voce dura...
''')
    else:
        break