import requests
import json
import os
from dotenv import load_dotenv

from AcessTokenAD import get_access_token


def execute_dax_query():
    # Configuração das credenciais e o post com a query DAX
    load_dotenv()
    dataset_id = os.environ.get('dataset_id')
    group_id = os.environ.get('group_id')
    impersonatedUserName = os.environ.get('impersonatedUserName')
    
    dax_query = {
        "queries": [
            {
                "query": "EVALUATE ResumoExportao"
            }
        ],
        "serializerSettings": {
            "includeNulls": "true"
        },
        "impersonatedUserName": impersonatedUserName
    }
    
    # Obtendo o token de acesso
    access_token = get_access_token()
    
    # endpoint para a execução da query
    query_url = f'https://api.powerbi.com/v1.0/myorg/groups/{group_id}/datasets/{dataset_id}/executeQueries'
    
    # headers do endpoint
    query_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    
    # Execute the DAX query
    query_response = requests.post(query_url, headers=query_headers, data=json.dumps(dax_query))
    if query_response.status_code != 200:
        raise Exception(f'falha ao executar a query: {query_response.status_code} - {query_response.text}')
    
    json_response = query_response.json()
    
    # Extraindo valores da resposta e colocando em uma lista
    values = []
    for table in json_response['results'][0]['tables']:
        for row in table['rows']:
            values.extend(row.values())
    
    return values

if __name__ == "__main__":
   print( execute_dax_query() )