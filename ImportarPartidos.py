import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from datetime import date
from datetime import datetime
from dotenv import load_dotenv

def importacao():
    load_dotenv()
    print('Iniciando procedimento de raspagem de dados do site do TSE...')

    # Configurações do navegador Chrome para rodar em modo headless
    options = Options()
    #options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    # Acessa a página principal do site do TSE
    driver.get('https://sapf.tse.jus.br/sapf-consulta/paginas/principal')

    # Aguarda e clica no link para a página de partidos em formação
    Pagina1 = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="PrincipalForm"]/ul/li[2]/a')))
    Pagina1.click()

    # Seleciona a opção de exibir 100 partidos por página
    Selecao = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="partidoDataList:j_id2"]')))
    Drop = Select(Selecao)
    Drop.select_by_visible_text('100')

    # Espera carregar todos os partidos
    time.sleep(10)
    Total_Partidos = WebDriverWait(driver, 60).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="partidoDataList_data"]/tr')))
    Qtd_Partidos = len(Total_Partidos)
    print(f'Total de partidos em formação: {str(Qtd_Partidos)}')

    hoje = date.today()
    Estados = []

    # Loop através de cada partido para coletar dados detalhados
    for i in range(Qtd_Partidos):
        Selecao = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="partidoDataList:j_id2"]')))
        Drop = Select(Selecao)
        Drop.select_by_visible_text('100')

        # Rola a página para baixo
        time.sleep(10)
        webdriver.ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()

        # Obtém o nome do partido
        Nome = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,
            '//*[@id="partidoDataList_data"]/tr[' + str(i + 1) + ']/td[1]'))).get_attribute("innerHTML")

        # Clica no link para os detalhes do partido
        Pagina2 = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="partidoDataList:' + str(i) +':j_idt36"]')))
        Pagina2.click()

        # Coleta dados de cada estado
        Count = 0
        while Count <= 26:
            Estado = {
                "Nome": Nome,
                "Data": str(hoje),
                "Estado": WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,
                    '//*[@id="j_idt42:' + str(Count) + ':j_idt44_header"]/span'))).get_attribute("innerHTML"),
                "Apoiamentos": WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,
                    '//*[@id="j_idt42:' + str(Count) + ':j_idt44_content"]/table/tbody/tr/td'))).get_attribute("innerHTML").strip(),
            }
            Estados.append(Estado)
            Count += 1

        # Volta para a página de lista de partidos
        Voltar = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="DetalharPartidosForm"]/div[4]/input')))
        webdriver.ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        Voltar.click()
        print(str(i + 1) + ' de ' + str(Qtd_Partidos) + ' - Partido em formação: ' + Nome + ': raspagem concluída. ')

    # Define o caminho e o nome do arquivo CSV
    data = str((hoje.year * 10000) + (hoje.month * 100) + hoje.day)
    caminho = os.environ.get('caminho')
    arquivo = caminho + data + '.csv'

    print('Gravando arquivo ".csv"')

    # Função para escrever o cabeçalho no arquivo CSV
    def Cabecalho():
        with open(arquivo, 'a+', newline='', encoding='utf-8') as output_file:
            keys = ['Nome', 'Data', 'Estado', 'Apoiamentos']
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()

    # Função para escrever as linhas de dados no arquivo CSV
    def Linhas():
        with open(arquivo, 'a+', newline='', encoding='utf-8') as output_file:
            keys = ['Nome', 'Data', 'Estado', 'Apoiamentos']
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writerows(Estados)

    # Tenta remover o arquivo existente e criar um novo com cabeçalho, em seguida adiciona os dados
    try:
        os.remove(arquivo)
        Cabecalho()
    except:
        Cabecalho()
    Linhas()
    
    # Fecha o navegador e finaliza a raspagem
    driver.quit()

    agora = datetime.now()
    data_e_hora_em_texto = agora.strftime('%d/%m/%Y %H:%M')
    print(f'Execução da importação realizada com sucesso, data_hora: {data_e_hora_em_texto}')
    print('\n==================================================================================================\n')

if __name__ == "__main__":
    importacao()