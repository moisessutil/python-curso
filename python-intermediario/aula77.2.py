perguntas = [
    {
        'pergunta' : 'Quanto é 2 + 2?',
        'opcoes' : ['0', '10', '4', '8'],
        'resposta' : '2',
    },
    {
        'pergunta' : 'Quanto é 2 * 8?',
        'opcoes' : ['20', '16', '48', '12'],
        'resposta' : '1',
    },
    {
        'pergunta' : 'Ohh James eu quero uma:',
        'opcoes' : ['Salada', 'Arma carregada', 'Pirocada', 'Salada de Fruta'],
        'resposta' : '3',
    },
    {
        'pergunta' : 'Meu heroi ele não usa capa ele usa:',
        'opcoes' : ['Maconha porraa', 'Arma', 'Habilidade', 'Sabedoria'],
        'resposta' : '0',
    },
]

contador = 0
for i in range(len(perguntas)):
    res = perguntas[i]['resposta']
    print(perguntas[i]['pergunta'])
    print()

    for num, i in enumerate(perguntas[i]['opcoes']):
        print(f'{num})', i)

    print()
    resposta = input('Selecione um opção: ')
    
    if resposta == res:
        print('Acertou 👍')
        contador += 1
    else:
        print('Errou ❌')

    print('-' *100)

print(f'Parabéns vc acertou {contador} de {len(perguntas)} perguntas')