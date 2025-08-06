from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

#config do navegador
driver = webdriver.Chrome()

#abrir page de login do sistema
driver.get("https://smart.sgisistemas.com.br/login")

#breve espera ate a abertura do sistema
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "usuario"))
)

username_input.send_keys("")

#breve espera ate o campo senha aparecer na página
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "senha"))
)

password_input.send_keys("")

#breve espera ate o botão ser login seja clicável
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "botao_submit"))
)

login_button.click()

#espera pra processamento de login
time.sleep(10)

#selecionar o cd como filial
filial_select = WebDriverWait(driver, 8).until(
    EC.presence_of_element_located((By.ID, "filial_id"))
)
select = Select(filial_select)
select.select_by_value("15")

#procurar prosseguir by ID
prosseguir_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "botao_prosseguir_informa_local_trabalho"))
)

prosseguir_button.click()

#breve espera para carregamento da page
time.sleep(5)

#ir ate a page de liberacao de encomendas
driver.get("https://smart.sgisistemas.com.br/liberacoes_vendas")

#breve espera para carregamento da page
time.sleep(5)

#identify a tabela de encomendas e os links de edição
links_edicao = driver.find_elements(By.XPATH, '//td[@class="campo_id"]/a')

#clicar nos links de edição (por exemplo, nos primeiros 5 links)
for link in links_edicao[:5]:
    try:
        link.click()
        #aguardar a page de edição carregar
        time.sleep(3)
        
        #checar a descricao do item
        descricao_items = driver.find_elements(By.XPATH, '//table[@class="table table-bordered table-hover table-striped sortable-theme-bootstrap"]/tbody/tr/td[1]/span')
        
        rejeitar = False
        for descricao_item in descricao_items:
            descricao_text = descricao_item.text
            if '*' in descricao_text or '**' in descricao_text:
                rejeitar = True
                break
        
        if rejeitar:
            #rejeitar encomenda
            status_select = Select(driver.find_element(By.ID, 'status'))
            status_select.select_by_value("rejeitado")
            print(f"Encomenda rejeitada devido a item fora do mix.")
        else:
            #autorizar encomenda
            status_select = Select(driver.find_element(By.ID, 'status'))
            status_select.select_by_value("autorizado")
            print(f"Encomenda autorizada.")
        
        salvar_button = driver.find_element(By.XPATH, '//input[@value="Salvar"]')
        salvar_button.click()
        
        #voltar pra page de liberacao de encomendas
        driver.get("https://smart.sgisistemas.com.br/liberacoes_vendas")
        time.sleep(5)
    except Exception as e:
        print(f"Erro ao processar encomenda: {e}")

input("Pressione Enter para fechar o navegador...")

driver.quit()