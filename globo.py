from selenium import webdriver
import pandas as pd
import time

def globo(data_inicial, data_final):
    datas = pd.date_range(data_inicial,data_final,freq='M')    
    driver = webdriver.Chrome()
    driver.maximize_window()
    df = {}
    for i in datas:
        ano = i.strftime('%Y')
        mes = i.strftime('%m')
        link = \
        'https://acervo.oglobo.globo.com/busca/?tipoConteudo=pagina&ordenacaoData=relev\
        ancia&allwords=+corrup%C3%A7%C3%A3o&anyword=&noword=&exactword=&decadaSeleciona\
        da=2010&anoSelecionado={}&mesSelecionado={}&matutino=on&economia=on&pais=on&ri\
        o=on&opiniao=on&primeirapagina=on&segundapagina=on'.format(ano,mes)
        driver.get(link)
        x = None
        for j in ['4','5']:
            try:
                time.sleep(2)
                x = driver.find_element_by_xpath('/html/body/div[{}]/div[1]/div[1]'.format(j)).text
                print(x)
            except Exception as e:
                print(e, 'at', i)
                pass
            try:
                x = x.split('\n')[0]
            except AttributeError:
                pass
            try:
                x = int(x)
                break
            except ValueError:
                continue
            except TypeError:
                break
        df.update({i : x})
        time.sleep(5)
        
    s = pd.Series(df)
    return s