import os
from dotenv import load_dotenv
import requests
from AcessTokenAD import get_access_token


def refresh_dataset():

    load_dotenv()

    DATASET_ID =  os.environ.get('dataset_id')
    GROUP_ID = os.environ.get('group_id')

    REFRESH_URL = f"https://api.powerbi.com/v1.0/myorg/groups/{GROUP_ID}/datasets/{DATASET_ID}/refreshes"

    token = get_access_token()

    """Solicita a atualização do dataset no Power BI."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(REFRESH_URL, headers=headers)
    if response.status_code == 202:
        print("Atualização do dataset iniciada com sucesso!")
    else:
        print("Erro ao atualizar o dataset:", response.json())

if __name__ == "__main__":
    refresh_dataset()
    