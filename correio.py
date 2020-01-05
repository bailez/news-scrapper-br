from selenium import webdriver
import pandas as pd
import time

def correio(palavra, data_inicial, data_final):
    datas = pd.date_range(data_inicial,data_final,freq='M')    
    df = {}
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(r'https://www.correiobraziliense.com.br/busca/')
    
    for i in datas:
        data_inicial = '01/' + i.strftime('%m') + '/' + i.strftime('%Y')
        data_final = i.strftime('%d') + '/' + i.strftime('%m') + '/' + i.strftime('%Y')

        for k in range(2):
            try:
                driver.find_element_by_xpath('//*[@id="txt-search-simple"]').clear()
                driver.find_element_by_xpath('//*[@id="txt-search-simple"]').send_keys(palavra)
                # avançada
                driver.find_element_by_xpath('//*[@id="search-advanced-item"]').click()            
                #Política Brasil Economia
                driver.find_element_by_xpath('//*[@id="search-advanced-sections"]/div[3]/label/span').click()
                #Cidades
                driver.find_element_by_xpath('//*[@id="search-advanced-sections"]/div[4]/label/span').click()
                #Economia
                driver.find_element_by_xpath('//*[@id="search-advanced-sections"]/div[5]/label/span').click()
                #Especiais
                driver.find_element_by_xpath('//*[@id="search-advanced-sections"]/div[10]/label/span').click()
                #Política
                driver.find_element_by_xpath('//*[@id="search-advanced-sections"]/div[9]/label/span').click()
                #Brasil
                driver.find_element_by_xpath('//*[@id="search-advanced-sections"]/div[16]/label/span').click()
                #Capa do dia
                driver.find_element_by_xpath('//*[@id="search-advanced-sections"]/div[14]/label/span').click()
                #Opinião
                driver.find_element_by_xpath('//*[@id="search-advanced-sections"]/div[15]/label/span').click()
                #Últimas notícias
                driver.find_element_by_xpath('//*[@id="search-advanced-sections"]/div[34]/label/span').click()
                #inicio
                driver.find_element_by_xpath('//*[@id="search-advanced-date-from"]').send_keys(data_inicial)
                #fim
                driver.find_element_by_xpath('//*[@id="search-advanced-date-to"]').send_keys(data_final)
                #%pesquisar
                driver.find_element_by_xpath('//*[@id="btn-search-refresh-results"]/span').click()
                driver.find_element_by_xpath('//*[@id="btn-search-simple"]').click()
                break
            except Exception:
                continue
        x = None
        for j in range(3):
            time.sleep(4)
            x = driver.find_element_by_xpath('//*[@id="search-h1"]').text
            print(x)
            if x == '453.218 resultados':
                time.sleep(1)
                continue
            else:
                break
        x = x.split(' ')[0]
        try:
            x = int(x)
        except ValueError:
            x = int(0)
        except TypeError:
            x = None
        df.update({i : x})
    s = pd.Series(df)
    return s.resample('M').last()