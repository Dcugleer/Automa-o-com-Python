import pyautogui
import time
import pandas as pd

# Configuração do PyAutoGUI
pyautogui.PAUSE = 1

def abrir_chrome(url):
    """Abre o navegador Chrome e acessa a URL fornecida."""
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    
    time.sleep(2)  # Pequeno delay para garantir que o Chrome abriu
    pyautogui.write(url)
    pyautogui.press("enter")
    
    time.sleep(3)  # Aguarda o carregamento da página

def realizar_login(email, senha, pos_email=(448, 374)):
    """Realiza login no site."""
    pyautogui.click(*pos_email)
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("tab")
    pyautogui.press("enter")

def preencher_formulario(tabela, posicao_campo=(508, 264)):
    """Preenche o formulário com os dados da tabela CSV."""
    for _, produto in tabela.iterrows():
        pyautogui.click(*posicao_campo)

        campos = ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo", "obs"]
        for campo in campos:
            valor = str(produto[campo])
            if pd.notna(valor):  # Verifica se o valor não é NaN
                pyautogui.write(valor)
            pyautogui.press("tab")

        pyautogui.press("enter")
        pyautogui.scroll(10000)

def main():
    url_login = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    email = "Teste@gmail.com"
    senha = "minhasenha"
    
    abrir_chrome(url_login)
    realizar_login(email, senha)

    tabela_produtos = pd.read_csv("produtos.csv")
    print(tabela_produtos)
    
   
