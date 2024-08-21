from TextoTwitter import corpo
from ImageMatriz import tirar_screenshot_objeto
import os
from dotenv import load_dotenv
import tweepy

def twitt():
    # Carrega variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Obtém as credenciais de autenticação do Twitter a partir das variáveis de ambiente
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
    ACESS_TOKEN = os.environ.get('ACESS_TOKEN')
    ACESS_TOKEN_SECRET = os.environ.get('ACESS_TOKEN_SECRET')
    BEARER_TOKEN = os.environ.get('BEARER_TOKEN')

    # Cria um cliente do Tweepy para interação com a API do Twitter usando credenciais OAuth2
    client = tweepy.Client(
        consumer_key = CONSUMER_KEY,
        consumer_secret = CONSUMER_SECRET,
        access_token = ACESS_TOKEN,
        access_token_secret = ACESS_TOKEN_SECRET,
        bearer_token = BEARER_TOKEN
    )

    # Configura o método de autenticação OAuth1 para usar a API do Twitter
    auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACESS_TOKEN, ACESS_TOKEN_SECRET)

    # Cria uma instância da API do Tweepy com o método de autenticação configurado
    api = tweepy.API(auth)

    # Obtém o texto do tweet chamando a função corpo
    texto = corpo()

    # Captura uma imagem chamando a função tirar_screenshot_objeto
    imagem = tirar_screenshot_objeto()

    # Faz o upload da imagem para o Twitter
    media = api.media_upload(imagem)

    # Cria e posta o tweet com o texto e a imagem carregada
    client.create_tweet(text=texto, media_ids=[media.media_id])
    
    # Imprime uma mensagem de confirmação no console
    print("Tweet postado com sucesso.")
    print('\n==================================================================================================\n')

if __name__ == "__main__":
    twitt()