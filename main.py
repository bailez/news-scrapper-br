from selenium import webdriver
import pandas as pd
import time
df = {}
def folha(palavra, data_inicial, data_final):
    datas = pd.date_range(data_inicial,data_final,freq='d')
    driver = webdriver.Chrome(r'D:\chromedriver_win32\chromedriver.exe')
    driver.maximize_window()

    for i in datas:        
        day = i.strftime('%d')
        month = i.strftime('%M')
        year = i.strftime('%Y')
        for k in range(3):
            try:
                driver.get(r'https://acervo.folha.com.br/busca-avancada.do')
                driver.find_element_by_xpath('//*[@id="advanced-search-form"]/div[1]/div/div[1]/input').clear()
                driver.find_element_by_xpath('//*[@id="advanced-search-form"]/div[1]/div/div[1]/input').send_keys(palavra)
                #Data'
                driver.find_element_by_xpath('//*[@id="advanced-search-form"]/div[2]/div[1]/div[2]').click()
                #dia
                driver.find_element_by_xpath('//*[@id="modo-por-dia"]/div[1]/input').send_keys(day)
                #mes
                driver.find_element_by_xpath('//*[@id="modo-por-dia"]/div[2]/input').send_keys(month)
                #ano
                driver.find_element_by_xpath('//*[@id="modo-por-dia"]/div[3]/input').send_keys(year)
                #Temas
                driver.find_element_by_xpath('//*[@id="selecione-temas"]').click()
                driver.find_element_by_xpath('//*[@id="filtertheme"]/div[1]/label').click()
                #Jornais
                driver.find_element_by_xpath('//*[@id="selecione-jornais"]').click()
                driver.find_element_by_xpath('//*[@id="advanced-search-form"]/div[3]/div/div[1]/div/div/div[1]/label').click()
                #Cadernos
                driver.find_element_by_xpath('//*[@id="selecione-cadernos"]').click()
                driver.find_element_by_xpath('//*[@id="field-cadernos"]/div[1]/label').click()        
                #Buscar
                driver.find_element_by_xpath('//*[@id="advanced-search-form"]/button').click()
                break
            except Exception:
                continue
        x = None
        for tries in range(3):
            try:
                time.sleep(3)
                x = driver.find_element_by_xpath('/html/body/main/div[1]/section/div[1]/span').text
                continue
            except Exception:
                continue
        print(x)
        try:
            x = x.split(' ')[0]
            try:
                x = int(x)
            except ValueError:
                x = int(0)
        except:
            pass
        df.update({i : x})
    s = pd.Series(df)
    return s.resample('M').last()
# %%
inicio = '01-01-2010'
fim = '12-01-2019'
x =folha('corrupção',inicio,fim)
x.to_csv(r'D:\Dados\folha.csv')
     