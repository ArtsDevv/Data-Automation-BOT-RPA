import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Entrar no sistema

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("win", "up")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)

# Login

pyautogui.click(x=6806, y=1622)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("logtype")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)

# Abrir produtos.csv

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=653, y=294)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]

    if obs != "nan":
        pyautogui.write(str(tabela.loc[linha, "obs"]))
        
    pyautogui.press("tab")
    pyautogui.press("enter") 
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos
