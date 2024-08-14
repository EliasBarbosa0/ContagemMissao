
import time
from pytz import timezone
from ImportarPartidos import importacao  # Importa a função de importação do módulo ImportarPartidos
from apscheduler.schedulers.blocking import BlockingScheduler  # Importa o agendador de tarefas
from Twitter_Bot import twitt

print(f'Executando agendamento, as importações ocorrerão nos horários previstos.')

# Cria uma instância do agendador
scheduler = BlockingScheduler(timezone=timezone('America/Sao_Paulo'))

# Define a função que será agendada
def tarefa():
    try:
        importacao()

    except:
        print('Ocorreu um erro na importação')
    
    finally:
        time.sleep(420)
        try:
            twitt()
        except:
            print('Ocorreu um erro ao twittar')

def tarefa2():
    try:
        importacao()

    except:
        print('Ocorreu um erro na importação')

    
# Define o tempo de tolerância de 60 segundos
misfire_grace_time = 60

# Adiciona a tarefa ao agendador para ser executada em horários específicos durante os dias da semana
scheduler.add_job(tarefa, 'cron', day_of_week='mon-fri', hour=9, minute=0, misfire_grace_time=misfire_grace_time)
scheduler.add_job(tarefa, 'cron', day_of_week='mon-fri', hour=10, minute=0, misfire_grace_time=misfire_grace_time)
scheduler.add_job(tarefa, 'cron', day_of_week='mon-fri', hour=11, minute=0, misfire_grace_time=misfire_grace_time)
scheduler.add_job(tarefa, 'cron', day_of_week='mon-fri', hour=12, minute=0, misfire_grace_time=misfire_grace_time)
scheduler.add_job(tarefa, 'cron', day_of_week='mon-fri', hour=13, minute=0, misfire_grace_time=misfire_grace_time)
scheduler.add_job(tarefa, 'cron', day_of_week='mon-fri', hour=14, minute=0, misfire_grace_time=misfire_grace_time)
scheduler.add_job(tarefa, 'cron', day_of_week='mon-fri', hour=15, minute=0, misfire_grace_time=misfire_grace_time)
scheduler.add_job(tarefa, 'cron', day_of_week='mon-fri', hour=16, minute=0, misfire_grace_time=misfire_grace_time)
scheduler.add_job(tarefa, 'cron', day_of_week='mon-fri', hour=17, minute=0, misfire_grace_time=misfire_grace_time)
scheduler.add_job(tarefa, 'cron', day_of_week='mon-fri', hour=18, minute=0, misfire_grace_time=misfire_grace_time)
scheduler.add_job(tarefa, 'cron', day_of_week='mon-fri', hour=19, minute=0, misfire_grace_time=misfire_grace_time)
scheduler.add_job(tarefa, 'cron', day_of_week='mon-fri', hour=20, minute=0, misfire_grace_time=misfire_grace_time)
scheduler.add_job(tarefa, 'cron', day_of_week='mon-fri', hour=21, minute=0, misfire_grace_time=misfire_grace_time)
scheduler.add_job(tarefa2, 'cron', day_of_week='sat', hour=10, minute=0, misfire_grace_time=misfire_grace_time)  # Sábado às 10:00
scheduler.add_job(tarefa2, 'cron', day_of_week='sun', hour=10, minute=0, misfire_grace_time=misfire_grace_time)  # Domingo às 10:00

# Inicia o agendador para começar a executar as tarefas nos horários definidos
scheduler.start()