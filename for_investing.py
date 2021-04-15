def aceptar_cookies():
    from selenium import webdriver

    """ Esta función recibe una url de investing.com y acepta las cookies"""
    html = driver.get(urlprevia) #version del request de selenium, abrir página
    url= driver.find_element_by_id("onetrust-accept-btn-handler").click() #y empezamos a navegar, en este caso aceptamos cookies
    return url

def seleccionar_6_meses():
    """ Esta funcion recibe como argumento una páginca concreta de investing y selecciona los ultimos 6 meses en el calendario"""
    from selenium import webdriver
    import time
    
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



    
    driver.find_element_by_xpath ("/html/body/div[7]/div[2]/div/a[1]/span").click() #echamos los meses hacia atrás #mejorable a que la funcion reciba meses
    driver.find_element_by_xpath ("/html/body/div[7]/div[2]/div/a[1]/span").click()
    driver.find_element_by_xpath ("/html/body/div[7]/div[2]/div/a[1]/span").click()
    driver.find_element_by_xpath ("/html/body/div[7]/div[2]/div/a[1]/span").click()
    driver.find_element_by_xpath ("/html/body/div[7]/div[2]/div/a[1]/span").click()

    driver.find_element_by_xpath ("/html/body/div[7]/div[2]/table/tbody/tr[1]/td[4]/a").click () #y clickamos en el día 1 #mejorable a current day-1

    driver.find_element_by_xpath ("/html/body/div[7]/div[3]/div/a[2]/span").click() #ahora los echamos hacia adelante
    driver.find_element_by_xpath ("/html/body/div[7]/div[3]/div/a[2]/span").click()
    driver.find_element_by_xpath ("/html/body/div[7]/div[3]/div/a[2]/span").click()
    driver.find_element_by_xpath ("/html/body/div[7]/div[3]/div/a[2]/span").click()
    driver.find_element_by_xpath ("/html/body/div[7]/div[3]/div/a[2]/span").click()

    driver.find_element_by_xpath ("/html/body/div[7]/div[3]/table/tbody/tr[3]/td[1]/a").click () #y clickamos en el ultimo dia habilitado

    calendario= driver.find_element_by_xpath ("/html/body/div[7]/div[5]/a").click () #aplicamos cambios en el calendario
    time.sleep(5)

    return calendario