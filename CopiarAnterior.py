import time
from RefreshDataset import refresh_dataset
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# caminho do arquivo
load_dotenv()
caminho_diretorio = os.environ.get('caminho')

# Obter o nome do arquivo baseado no dia anterior
data_anterior = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
input_file = os.path.join(caminho_diretorio, f"{data_anterior}.csv")

# Verificar se o arquivo existe
if not os.path.exists(input_file):
    print(f"Arquivo {input_file} não encontrado. Verifique o caminho e o nome do arquivo.")
else:
    # Gerar o nome do novo arquivo com base na data atual
    data_atual = datetime.now().strftime('%Y%m%d')
    novo_nome = f"{data_atual}.csv"
    output_file = os.path.join(caminho_diretorio, novo_nome)

    # Ler o arquivo CSV
    df = pd.read_csv(input_file)

    # Atualizar a data para o dia atual no arquivo
    df['Data'] = datetime.now().strftime('%Y-%m-%d')

    # Salvar o novo arquivo
    df.to_csv(output_file, index=False)

    print(f"Arquivo atualizado salvo como: {output_file}")

time.sleep(10)

refresh_dataset()