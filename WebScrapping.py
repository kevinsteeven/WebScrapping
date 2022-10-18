from selenium import webdriver
from selenium.webdriver.chrome.options import Options #Esta importacion permite modificar las configuraciones del webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

app_path = os.path.dirname(sys.executable) #obtener ruta del ejecutable
hoy= datetime.now()
#transformar la fecha a str, ver informacion sobre los formatos en doc de strftime
fechastr=hoy.strftime("%m%d%Y") #se esta usando formato mmddyyyy
website= 'https://www.thesun.co.uk/sport/football/'
pathChromedriver="/Users/natal/OneDrive/Documentos/cosasKevin/chromedriver/chromedriver_win32/chromedriver.exe"
#modificar paametro headless que la interaccion con el navegador se haga por background
options=Options()
options.headless=True
service= Service(executable_path=pathChromedriver)
driver=webdriver.Chrome(service=service, options=options) #el parametro options es opcional y se pasa por que se ajusta para activar el headless
driver.get(website)
#obtener divs de noticias en una lista
containers=driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')
titulos=[]
subtitulos=[]
links=[]
#recorrer lista de divs
for container in containers:
    titulo=container.find_element(by="xpath",value='./a/h2').text #titulos de noticias
    subtitulo=container.find_element(by="xpath",value='./a/p').text#subtitulos de noticias
    link=container.find_element(by="xpath",value='./a').get_attribute("href")#obtener link
    #agregar datos a las listas
    titulos.append(titulo)
    subtitulos.append(subtitulo)
    links.append(link)
#crear CSV

my_dict = {'titulos': titulos, 'subtitulos': subtitulos, 'links': links}
df_headlines = pd.DataFrame(my_dict)
nombre_archivo=f'noticias-{fechastr}.csv'
#formar ruta
final_path=os.path.join(app_path,nombre_archivo)

df_headlines.to_csv(final_path)

driver.quit()