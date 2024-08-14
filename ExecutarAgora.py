import time
from ImportarPartidos import importacao

from Twitter_Bot import twitt

def tarefa():
    # Tenta executar a importação dos dados
    try:
        importacao()
    except:
        # Captura e exibe uma mensagem de erro caso a importação falhe
        print('Ocorreu um erro na importação')
    finally:
        # Aguarda 420 segundos (7 minutos) antes de tentar postar o tweet
        time.sleep(420)
        try:
            twitt()
        except:
            # Captura e exibe uma mensagem de erro caso a postagem do tweet falhe
            print('Ocorreu um erro ao twittar')

def tarefa2():
    # Tenta executar a importação dos dados
    try:
        importacao()
    except:
        # Captura e exibe uma mensagem de erro caso a importação falhe
        print('Ocorreu um erro na importação')

def tarefa3():
    # Tenta postar o tweet
    try:
        twitt()
    except:
        # Captura e exibe uma mensagem de erro caso a postagem do tweet falhe
        print('Ocorreu um erro ao twittar')

# Exibe as opções de tarefas disponíveis para o usuário
print('1 - Importação dos dados + twitt.')
print('2 - Importação dos dados.')
print('3 - Twitt')

# Solicita que o usuário selecione uma tarefa para executar
selecao = input('Qual tarefa deseja executar?')

# Utiliza a instrução match para executar a tarefa selecionada pelo usuário
match selecao:
    case '1':
        # Executa a tarefa que inclui a importação dos dados e a postagem do tweet
        tarefa()
    case '2':
        # Executa a tarefa que inclui apenas a importação dos dados
        tarefa2()
    case '3':
        # Executa a tarefa que inclui apenas a postagem do tweet
        tarefa3()
    case _:
        # Exibe uma mensagem caso a opção selecionada não seja válida
        print('Opção não identificada')
