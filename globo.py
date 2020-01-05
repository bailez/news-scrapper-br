from selenium import webdriver
import pandas as pd
import time

def globo(data_inicial, data_final):
    datas = pd.date_range(data_inicial,data_final,freq='M')    
    df = {}
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    for i in datas:
        ano = i.strftime('%Y')
        mes = i.strftime('%m')
        link = \
        'https://acervo.oglobo.globo.com/busca/?tipoConteudo=pagina&ordenacaoData=relev\
        ancia&allwords=+corrup%C3%A7%C3%A3o&anyword=&noword=&exactword=&decadaSeleciona\
        da=2010&anoSelecionado={}&mesSelecionado={}&matutino=on&economia=on&pais=on&ri\
        o=on&opiniao=on&primeirapagina=on&segundapagina=on'.format(ano,mes)
        driver.get(link)
        time.sleep(3)
        for j in ['4','5']:
            try:
                x = driver.find_element_by_xpath('/html/body/div[{}]/div[1]/div[1]'.format(j)).text
            except Exception:
                pass
            
            x = x.split('\n')[0]
            try:
                x = int(x)
                break
            except ValueError:
                continue
        df.update({i : x})
    s = pd.Series(df)
    return s