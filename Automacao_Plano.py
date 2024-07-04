import pyautogui
import time
from colorama import init, Back

init()

# pyautogui.click ->  clicar em algum lugar
# pyautogui.write ->  escrever um texto
# pyautogui.press ->  pressionar UMA tecla no teclado
# pyautogui.hotkey ->  pressionar mais de UMA tecla no teclado

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("win","up")
pyautogui.write("https://plano.allstrategy.com.br")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1.5)
pyautogui.click(x=104, y=646) #Clicar em relatórios
time.sleep(2.1)
pyautogui.doubleClick(x=1544, y=343) #Clicar no campo pesquisa
time.sleep(0.8)
pyautogui.doubleClick(x=1544, y=343) #Clicar no campo pesquisa novamente (para poder digitar)
pyautogui.write("conse")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=376, y=411) #Clicar para abrir relatórios do Conselho
time.sleep(1)
pyautogui.click(x=1608, y=310) #Clicar no campo de pesquisa RELATORIO
pyautogui.write("COMPER")
pyautogui.press("enter")
pyautogui.click(x=624, y=452) #Abrir relatório Comper/Fort/Farma/Pera
time.sleep(2.5) #Tempo para gerar o relatório
print("Relatório Comper/Fort/Farma/Pera aberto")

def abrirFiltro():
    pyautogui.click(x=502, y=316) #Clicar para abrir filtros
    time.sleep(1)
    pyautogui.click(x=1011, y=243) #Clicar na opções de filtro

def abrirFiltro2():
    pyautogui.click(x=502, y=316) #Clicar para abrir filtros
    time.sleep(5)
    pyautogui.click(x=1032, y=244) #Clicar na opções de filtro

def cliquefiltro():
    pyautogui.click(x=1157, y=626) #Clicar na seta de baixo da rolagem 1 vez
    pyautogui.click(x=950, y=273) #Clicar na primeira opção de filtro

def salvarArquivos(x):
    time.sleep(4.2)
    pyautogui.click(x=1366, y=869) #Clicar em FILTRAR 1
    pyautogui.click(x=1366, y=894) #Clicar em FILTRAR 2
    time.sleep(8) #TEMPO PAUSA GERAR RELATÓRIO ----------------------------
    pyautogui.PAUSE = 0.8
    pyautogui.rightClick(x=855, y=392) #Clicar com o botão direito do mouse
    pyautogui.click(x=974, y=349) #Clicar para exportar
    pyautogui.PAUSE = 2
    pyautogui.click(x=832, y=360) #Clicar no campo para digitar o nome do arquivo
    pyautogui.write(x) #Escrever o nome do arquivo
    pyautogui.click(x=952, y=522) #Clicar em Salvar arquivo
    time.sleep(1.5)
    pyautogui.click(x=1068, y=522) #Clicar em Cancelar na pag de salvar arquivo

#Pausa entre todos os comandos do pyautogui

filtros = [
    "001 - COMPER_MS",
    "002 - COMPER_MT",
    "003 - COMPER_DF",
    "004 - COMPER_SC",
    "005 - FORT_MS",
    "006 - FORT_MT",
    "007 - FORT_DF",
    "008 - FORT_SC_NORTE",
    "009 - FORT_SC_GDEFLOR",
    "010 - FORT_SC_VLITAJAI",
    "011 - FORT_SC_OESTE",
    "012 - FORT_SC_SUL",
    "013 - FORT_SP",
    "014 - FORT_RS",
    "015 - FARMA_SC",
    "016 - FARMA_MT",
    "017 - FARMA_SP",
    "018 - FARMA_MS",
    "019 - PERA_TURISMO"]

pyautogui.PAUSE = 2

for bandeira in filtros:
    if bandeira =="001 - COMPER_MS":
        abrirFiltro()
        print(bandeira)
        pyautogui.click(x=950, y=273) #Clicar na primeira opção de filtro
    else:
        abrirFiltro2()
        print(bandeira)
        cliquefiltro()
    salvarArquivos(bandeira)

print('Download Comper, Fort, Farma e Pera Concluído.')


# Gerar relatórios do BATE FORTE

filtro_BF = ["020 - BF_MS", "021 - BF_MT", "022 - BF_DF", "023 - BF_VGP", "024 - BF_JCI"]

#Sair de um relatório e ir para o relatório do BF
pyautogui.click(x=357, y=281) # Clicar para retornar na tela anterior
pyautogui.doubleClick(x=1551, y=471) #Clicar no campo de pesquisa RELATORIO
time.sleep(0.8)
pyautogui.doubleClick(x=1551, y=471) #Clicar no campo de pesquisa RELATORIO novamente (para poder digitar)
pyautogui.write("BATE")
pyautogui.press("enter")
pyautogui.click(x=629, y=605) #Abrir relatório Bate Forte
time.sleep(1)

for bf_band in filtro_BF:
    print(bf_band)
    abrirFiltro2()
    cliquefiltro()
    salvarArquivos(bf_band)

print("Download BATEFORTE Concluído")

# Gerar relatórios do BROOKER/POSTO

filtro_B_POST = ["025 - BROKER","026 - POSTO_MT","027 - POSTO_MS"]

#Sair de um relatório e ir para o relatório do BROKER/POSTO
pyautogui.click(x=357, y=281) # Clicar para retornar na tela anterior
pyautogui.doubleClick(x=1551, y=471) #Clicar no campo de pesquisa RELATORIO
time.sleep(0.8)
pyautogui.doubleClick(x=1551, y=471) #Clicar no campo de pesquisa RELATORIO novamente (para poder digitar)
pyautogui.write("BROKER")
pyautogui.press("enter")
pyautogui.click(x=629, y=605) #Abrir relatório
time.sleep(1)

for brokerposto in filtro_B_POST:
    print(brokerposto)
    abrirFiltro2()
    cliquefiltro()
    salvarArquivos(brokerposto)

print("Download Broker e Posto Concluído")


#Gerar relatório PERLOG

#Sair de um relatório e ir para o relatório do PERLOG
pyautogui.click(x=357, y=281) # Clicar para retornar na tela anterior
pyautogui.doubleClick(x=1551, y=471) #Clicar no campo de pesquisa RELATORIO
time.sleep(0.8)
pyautogui.doubleClick(x=1551, y=471) #Clicar no campo de pesquisa RELATORIO novamente (para poder digitar)
pyautogui.write("PERLOG")
pyautogui.press("enter")
pyautogui.click(x=629, y=605) #Abrir relatório
time.sleep(1)

print("PERLOG")
abrirFiltro2()
cliquefiltro()
salvarArquivos("028 - PERLOG")
print("Download Perlog Concluído")



#Gerar relatório VUON

#Sair de um relatório e ir para o relatório do VUON
pyautogui.click(x=357, y=281) # Clicar para retornar na tela anterior
pyautogui.doubleClick(x=1551, y=471) #Clicar no campo de pesquisa RELATORIO
time.sleep(0.8)
pyautogui.doubleClick(x=1551, y=471) #Clicar no campo de pesquisa RELATORIO novamente (para poder digitar)
pyautogui.write("VUON")
pyautogui.press("enter")
pyautogui.click(x=629, y=605) #Abrir relatório
time.sleep(1)

print("VUON")
abrirFiltro2()
cliquefiltro()
salvarArquivos("029 - VUON")
print("Download VUON Concluído")


#Gerar relatório FDIC

#Sair de um relatório e ir para o relatório do FDIC
pyautogui.click(x=357, y=281) # Clicar para retornar na tela anterior
pyautogui.doubleClick(x=1551, y=471) #Clicar no campo de pesquisa RELATORIO
time.sleep(0.8)
pyautogui.doubleClick(x=1551, y=471) #Clicar no campo de pesquisa RELATORIO novamente (para poder digitar)
pyautogui.write("FDIC")
pyautogui.press("enter")
#pyautogui.click(x=594, y=596) #Abrir relatório
pyautogui.click(x=629, y=605) #Abrir relatório
time.sleep(1)

print("FDIC")
abrirFiltro2()
cliquefiltro()
salvarArquivos("030 - FDIC")
print("Download FDIC Concluído")


#Gerar relatório TRUDYS

#Sair de um relatório e ir para o relatório do COMPER (inclui o Trudys)
pyautogui.click(x=357, y=281) # Clicar para retornar na tela anterior
pyautogui.doubleClick(x=1551, y=471) #Clicar no campo de pesquisa RELATORIO
time.sleep(0.8)
pyautogui.doubleClick(x=1551, y=471) #Clicar no campo de pesquisa RELATORIO novamente (para poder digitar)
pyautogui.write("COMPER")
pyautogui.press("enter")
#pyautogui.click(x=594, y=596) #Abrir relatório
pyautogui.click(x=629, y=605) #Abrir relatório
time.sleep(1)

print("Trudys")
abrirFiltro2()
cliquefiltro()
salvarArquivos("031 - Trudys")
print("Download Trudys Concluído")

print(Back.GREEN + "Downloads 100% Concluídos!")
