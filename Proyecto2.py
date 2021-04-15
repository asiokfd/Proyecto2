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
import for_investing


driver = webdriver.Chrome() # indicamos al webdriver que navegador vamos a usar
driver.implicitly_wait(10) #le aplicamos un intervalo entre acciones

urlprevia = "https://www.investing.com/equities/facebook-inc" #esta es la pagina a scrapear


aceptar_cookies (urlprevia)

# buscamos el historial
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div[3]/nav/ul/li[3]/a").click() 
time.sleep (5)

#aplicamos una función para cambiar las fechas a las que nos interesan
seleccionar_6_meses (calendario)

# aquí nos quedamos con el body de la tabla, que es donde están los datos
bodytabla= driver.find_element_by_xpath ("/html/body/div[5]/section/div[9]/table[1]/tbody") 

#aplicamos funcion para pasar los datos a un DataFrame
sacando_tabla (bodytabla) 

#los guardamos 
df.to_csv (r"..\Data\facebook.csv")
# guardarlo en Jupyter Notebook me funciona, en VStudio no me dá problemas, pero solo consigo depurar el archivo, no runearlo realmente,
#  asi que no se si me funciona

# teoricamente cerramos el navegador, la verdad que no me funciona, no se si por lo mismo que lo anterior
driver.quit(); 

#cargamos los datas
resultados = pd.read_csv (r'..\Data\resultados.csv') #esto se podía scrapear también, pero la he descargado manualmente
historico = pd.read_csv (r'..\Data\facebook.csv')

# en líneas generales, vamos a estandárizarlos para poder unirlos

# le quitamos los ; a las columnas
resultados.columns = [ col.replace (";" , "") for col in resultados.columns] 

# hacemos que ambas tengan el mismo formato de fecha ( me daba problemas)
resultados ["Publicacion"] = pd.to_datetime ( resultados.Publicacion) 
historico ["Fecha"] = pd.to_datetime ( historico.Fecha)

# borro una columna que no e de donde ha salido
historico.drop (["Unnamed: 0"], axis=1, inplace=True) 

# creamos dos columnas con datos que me interesan para la visualización
historico ["var_intra"]= historico.Max - historico.Min
historico ["volatilidad"]= ((historico.var_intra *100)/ historico.Close).round(2) 

#igualamos el índice

historico.set_index("Fecha", drop=False, inplace=True)
resultados.set_index("Publicacion", drop=False, inplace=True) 

# los uno para obtener un data sobre el que trabajar
dff= historico.join (resultados, lsuffix='idx', rsuffix='idx')

# ahora vamos a quedarnos únicamente con los datos que nos sirvan para lo que nos interesa
dff.drop (["Fecha", "Close", "Open", "Max", "Min", "Periodo" ], axis=1, inplace=True)

# Esto está separado porque pensaba hacer una resta entre lo esperado y lo real, pero solo hay datos para 1 de los dos dias, asi que lo elimino también
dff.drop ([" BPA_esperado", "BPA", "Ingresos", "Ingresos_esperados"], axis=1, inplace=True)

dff= dff.fillna(0)

#reseteo index porque asi me aseguro de saltarme los días que no abrio la bolsa, si uso (fecha+10) no se si va a caer en sabado el resultado.

dff.reset_index (inplace=True)

#esto no lo incluyo en el ejecutable, pero es lo que utilizé para localizar las fechas que quería
#buscando_datos = dff.loc[:, "Publicacion"] != 0
#fechas = dff.loc[buscando_datos]
#fechas


dfrango20a=dff.iloc[31: 41] 
dfrango20b=dff.iloc[54: 69]
dfrango20c=dff.iloc[101: 121] 




