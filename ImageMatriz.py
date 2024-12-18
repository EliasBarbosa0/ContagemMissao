from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from PIL import Image
import os

def tirar_screenshot_objeto():
    url = 'https://app.powerbi.com/view?r=eyJrIjoiOTZlNWFhYTktN2Y1Yy00NjM1LWIzNDItZmIyMTY2N2FmMDY0IiwidCI6ImFkY2JiMThhLWE3NzEtNDU5OS04YjllLWFiM2IzNmE3NWY1MSJ9'
    xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container/transform/div/div[3]/div/div'  # Substitua pelo XPath do objeto

    # Configuração do Chrome WebDriver
    options = Options()
    options.add_argument("--headless=new")  # Executa no modo headless, se necessário
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1080, 1080)
    driver.get(url)
    
    try:
        # Espera até que o objeto esteja visível
        objeto = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        time.sleep(10)    
        # Certifique-se de que o elemento está totalmente visível
        driver.execute_script("arguments[0].scrollIntoView(true);", objeto)

        # Caminho temporário para salvar o screenshot
        temp_screenshot_path = 'temp_screenshot.png'

        # Captura de tela do próprio elemento e salva em um arquivo temporário
        objeto.screenshot(temp_screenshot_path)

        # Abre a imagem do arquivo temporário e converte para RGB para evitar problemas de transparência
        imagem_objeto = Image.open(temp_screenshot_path).convert("RGB")

        # Obtém as dimensões da imagem
        largura, altura = imagem_objeto.size

        # Calcula a nova área da imagem após o recorte
        nova_largura = largura - 125
        nova_altura = altura - 65

        # Define a caixa de recorte (left, top, right, bottom)
        caixa_recorte = (0, 0, nova_largura, nova_altura)
        
        # Recorta a imagem
        imagem_recortada = imagem_objeto.crop(caixa_recorte)

        # Salva a imagem recortada
        objeto_screenshot_path = 'screenshot_objeto_recortado.png'
        imagem_recortada.save(objeto_screenshot_path)

    finally:
        # Remove o arquivo temporário
        if os.path.exists(temp_screenshot_path):
            os.remove(temp_screenshot_path)
        
        # Fecha o WebDriver
        driver.quit()

    return objeto_screenshot_path

if __name__ == "__main__":
    tirar_screenshot_objeto()