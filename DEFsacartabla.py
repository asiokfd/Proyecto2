def sacando_tabla(bodytabla):
    ### En esta función el argumento es el cuerpo de una tabla de datos tomada del historial de cotizaciones de investing.com
    ### lo que haremos con ella será recorrer las filas para quedarnos con los valores de dentro y agruparlos en un diccionario, donde las keys serán
    ### las columnas de nuestro df.
    tabladatos=[]
    for dato in bodytabla.find_elements_by_tag_name("tr"):
        import time
        import pandas as pd
        fila=[d for d in dato.find_elements_by_tag_name ("td")]
        if len (fila)>1 :
            dia= {
                "Fecha": fila[0].text,
                "Close": fila[1].text,
                "Open": fila[2].text,
                "Max": fila [3].text,
                "Min": fila [4].text,
                "Vol": fila [5].text,
                "Var": fila [6].text
                }
            tabladatosfb.append (dia)
            time.sleep (10)
            df = pd.DataFrame(tabladatos)
    return df

