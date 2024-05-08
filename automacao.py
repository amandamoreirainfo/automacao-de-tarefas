import pyautogui
import time
import pandas as pd

pyautogui.PAUSE =  0.5

pyautogui.press("win")
pyautogui.write("Opera")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(5) 

#print(pyautogui.position())

pyautogui.click(x=737, y=451)
pyautogui.write("amandateste@gmail.com")
pyautogui.press("tab")
pyautogui.write("amandateste1")
#print(pyautogui.position())
pyautogui.click(x=943, y=648)


time.sleep(3)


tabela = pd.read_csv("produtos.csv")

#print(tabela)

#codigo       marca        tipo  categoria  preco_unitario  custo  
#print(pyautogui.position())

#for para percorrer as linhas da tabela
for linha in tabela.index:
    pyautogui.click(x=887, y=351)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    #verifica se existe informação em obs, caso contrario não preenche
    if not pd.isna(tabela.loc[linha,"obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(800)



