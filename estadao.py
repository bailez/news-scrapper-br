#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 18:35:05 2020

@author: bailez
"""

from selenium import webdriver
import pandas as pd
import time

def estadao(palavra,data_inicial,data_final):
    x = 0
    datas = pd.date_range(data_inicial,data_final,freq='M')    
    df = {}
    driver = webdriver.Chrome(r'C:\Users\filip\Downloads\chromedriver_win32\chromedriver')
    driver.maximize_window()

    for i in datas:
    
        ano = i.strftime('%Y')
        mes = i.strftime('%m')
        link = \
        'https://acervo.estadao.com.br/procura/#!/{}/Acervo//spo|nac/1/2010/{}/{}/Painel%20de%20Negócios\
        |Economia|Caderno%202|Politica|Cidades|Metr%C3%B3pole|E&N|Especial\
        |Primeira|Opini%C3%A3o|Editorial|Geral|Alias|Telejornal'.format(palavra,ano,mes)
        driver.get(link)
        driver.refresh()
        time.sleep(3)
        for j in range(1):    
            try:
                x = driver.find_element_by_xpath('//*[@id="resultado"]/h3').text
            except Exception:
                pass
            try:
                x = x.split('Exibindo ')[1]
            except AttributeError:
                pass
            try:
                x = x.split(' ')[0]
            except AttributeError:
                pass
            try:
                x = int(x)
                break
            except ValueError:
                continue
        df.update({i : x})
    s = pd.Series(df)
    return s