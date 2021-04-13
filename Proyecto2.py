import pandas as pd
import os
import numpy as np
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time
driver = webdriver.Chrome()
from src import sacando_tabla

driver = webdriver.Chrome() # indicamos al webdriver que navegador vamos a usar
driver.implicitly_wait(10) #le aplicamos un intervalo entre acciones

urlprevia = "https://www.investing.com/equities/facebook-inc" #esta es la pagina a scrapear
html = driver.get(urlprevia) #version del request de selenium
url= driver.find_element_by_id("onetrust-accept-btn-handler").click() #y empezamos a navegar, en este caso aceptamos cookies

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div[3]/nav/ul/li[3]/a").click() #buscamos el historial
time.sleep (5)
driver.find_element_by_xpath ("/html/body/div[5]/section/div[8]/div[3]/div/div[1]/div[1]/div").click () #abrimos el calendario
time.sleep(5)
randomplace= driver.find_element_by_xpath ("/html/body/div[5]/section/ul[1]/li[6]/a")
randomplace2=driver.find_element_by_xpath ("/html/body/div[5]/section/ul[1]/li[3]/a")
webdriver.ActionChains(driver).move_to_element(randomplace).perform()
time.sleep (15)
webdriver.ActionChains(driver).move_to_element(randomplace2).perform()
time.sleep(5)

randomplace3=driver.find_element_by_xpath ("/html/body/div[7]/div[2]/div/a[1]/span")
webdriver.ActionChains(driver).move_to_element(randomplace3).perform()
#las ultimas lineas son moviendo el cursor a ver si salta un banner, parece que no salta




driver.find_element_by_xpath ("/html/body/div[7]/div[2]/div/a[1]/span").click() #echamos los meses hacia atrás
driver.find_element_by_xpath ("/html/body/div[7]/div[2]/div/a[1]/span").click()
driver.find_element_by_xpath ("/html/body/div[7]/div[2]/div/a[1]/span").click()
driver.find_element_by_xpath ("/html/body/div[7]/div[2]/div/a[1]/span").click()
driver.find_element_by_xpath ("/html/body/div[7]/div[2]/div/a[1]/span").click()

driver.find_element_by_xpath ("/html/body/div[7]/div[2]/table/tbody/tr[1]/td[4]/a").click () #y clickamos en el día 1

driver.find_element_by_xpath ("/html/body/div[7]/div[3]/div/a[2]/span").click() #ahora los echamos hacia adelante
driver.find_element_by_xpath ("/html/body/div[7]/div[3]/div/a[2]/span").click()
driver.find_element_by_xpath ("/html/body/div[7]/div[3]/div/a[2]/span").click()
driver.find_element_by_xpath ("/html/body/div[7]/div[3]/div/a[2]/span").click()
driver.find_element_by_xpath ("/html/body/div[7]/div[3]/div/a[2]/span").click()

driver.find_element_by_xpath ("/html/body/div[7]/div[3]/table/tbody/tr[3]/td[1]/a").click () #y clickamos en el ultimo dia habilitado

driver.find_element_by_xpath ("/html/body/div[7]/div[5]/a").click () #aplicamos cambios en el calendario
time.sleep(5)
bodytabla= driver.find_element_by_xpath ("/html/body/div[5]/section/div[9]/table[1]/tbody") # aquí nos quedamos con el body de la tabla, que es donde están los datos


sacando_tabla (bodytabla) #aplicamos funcion para pasar los datos a un DataFrame

df.to_csv (r"Data/facebook.csv") #los guardamos
driver.quit(); #y teoricamente cerramos el navegador, la verdad que no me funciona

resultados = pd.read_csv (r'Data\resultados.csv') #cargamos los datas
historico = pd.read_csv (r'Data\facebook.csv')
resultados.columns = [col.replace(";", "") for col in resultados.columns] # le quitamos los ; a las columnas

historico.drop (["Unnamed: 0"], axis=1, inplace=True) #borro una columna que no se de donde ha salido
historico ["var_intra"]= historico.Max - historico.Min
historico ["volatilidad"]= ((historico.var_intra *100)/ historico.Close).round(2) #creamos dos columnas con datos que me interesan para la visualización
