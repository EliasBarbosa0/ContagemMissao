import time
from ImportarPartidos import importacao
from Twitter_Bot import twitt

def executar_tarefa(importar=False, tweet=False):
    try:
        if importar:
            importacao()
        if tweet:
            if importar:
                time.sleep(420)
            twitt()
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Exibe as opções de tarefas disponíveis para o usuário
print('1 - Importação dos dados + Twitt.')
print('2 - Importação dos dados.')
print('3 - Twitt')

# Solicita que o usuário selecione uma tarefa para executar
selecao = input('Qual tarefa deseja executar?')

# Dicionário mapeando a seleção do usuário para as ações a serem realizadas
opcoes = {
    '1': {'importar': True, 'tweet': True},
    '2': {'importar': True, 'tweet': False},
    '3': {'importar': False, 'tweet': True},
}

# Executa a tarefa correspondente à seleção do usuário, ou exibe uma mensagem de erro se a seleção for inválida
if selecao in opcoes:
    executar_tarefa(**opcoes[selecao])
else:
    print('Opção não identificada')