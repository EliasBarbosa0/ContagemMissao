import requests
import os
from dotenv import load_dotenv

def get_access_token():
    # Define as credenciais do Microsoft Entra
    load_dotenv()
    tenant_id = os.environ.get('tenant_id')
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    
    # Define o endpoint do Microsot Entra para a obtenção do Token
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    
    # Define o header e os parametros do body
    token_headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    token_body = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://analysis.windows.net/powerbi/api/.default'
    }
    
    # Obtem o bearer token
    token_response = requests.post(token_url, headers=token_headers, data=token_body)
    if token_response.status_code != 200:
        raise Exception(f"Falha ao obter token: {token_response.status_code} - {token_response.text}")
    
    return token_response.json().get('access_token')