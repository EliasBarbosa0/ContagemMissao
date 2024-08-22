import time
from pytz import timezone
from ImportarPartidos import importacao
from apscheduler.schedulers.blocking import BlockingScheduler
from Twitter_Bot import twitt

print(f'Executando agendamento, as importações ocorrerão nos horários previstos.')

# Cria uma instância do agendador
scheduler = BlockingScheduler(timezone=timezone('America/Sao_Paulo'))

# Define a função que será agendada
def executar_tarefa(twitter=False):
    try:
        importacao()
        if twitter:
            time.sleep(420)
            twitt()
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Define o tempo de tolerância de 60 segundos
misfire_grace_time = 60

# Horários para os dias úteis (segunda a sexta)
horarios_dias_uteis = range(9, 22)
# Horários para o fim de semana
horarios_fim_de_semana = [(10, False), (21, False)]

# Agendamento para dias úteis com Twitter
for hora in horarios_dias_uteis:
    scheduler.add_job(executar_tarefa, 'cron', day_of_week='mon-fri', hour=hora, minute=0, misfire_grace_time=misfire_grace_time, kwargs={'twitter': True})

# Agendamento para o fim de semana sem Twitter
for hora, twitter in horarios_fim_de_semana:
    scheduler.add_job(executar_tarefa, 'cron', day_of_week='sat,sun', hour=hora, minute=0, misfire_grace_time=misfire_grace_time, kwargs={'twitter': twitter})

# Inicia o agendador para começar a executar as tarefas nos horários definidos
scheduler.start()