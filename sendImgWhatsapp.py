import pyautogui as pyg
import pyperclip as pyp
import time
import os

path = "NovasImagens/"
img_list = os.listdir(path)
image_path = f"{path}{img_list[0]}"
# print(img_list[:3])

# FAZ O ALT + TAB PARA O WHATSAPP
pyg.hotkey("alt", "tab")

time.sleep(0.4)
for i in img_list:
    print(i)
    # CLICA NO BT DE + AO LADO DA TEXT BOC
    bt_plus = x, y = 430, 690
    pyg.click(bt_plus)

    # CORRE COM O CURSOR PARA CIMA ATÉ O BOTÃO DE ANEXAR 
    for t in range(5):
        pyg.keyDown("up")

    # CLICA NO BOTÃO DE ANEXAR
    pyg.keyDown("enter")
    time.sleep(1)

    pyp.copy(i)
    # COLA O NOME DA IMAGEM NO CAMPO DE PESQUISA
    pyg.hotkey("ctrl", "v")
    # SELECIONA A IMAGE
    pyg.press("enter")
    time.sleep(1)
    # COLA O NOME DA IMAGEM NA LEGENDA DA IMAGEM
    pyg.hotkey("ctrl", "v")
    # ENVIA A IMAGEM
    pyg.press("enter")
    time.sleep(3)

