# Lista de tarefa
import json

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)

    print(f'Tarefa {tarefa} foi removida na lista')


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para refazer')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

    print(f'Tarefa {tarefa} foi readicionada na lista')


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Lista de Tarefas vazia')
        return
    
    tarefas.append(tarefa)

    print(f'Tarefa {tarefa} foi adicionada na lista')

def ler(tarefas, caminho_arquivo):
    dados = []

    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        print('arquivo não existe!')
        salvar(tarefas, caminho_arquivo)

    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas

    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
            dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)

    return dados

CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: salvar, listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        print()
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        print()
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        print()
        continue
    elif tarefa == 'salvar':
        salvar(tarefas, CAMINHO_ARQUIVO)
    else:
        adicionar(tarefa, tarefas)
        print()
        continue