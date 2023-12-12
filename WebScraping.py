import requests
from bs4 import BeautifulSoup
import pandas as pd

nombres =list()
apellidos =list()
especialidad = list()
url= 'http://127.0.0.1:8000/'
html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text,'html.parser')

#print(soup.prettify())
titulo = soup.find_all('title')
print (titulo)
data = soup.find_all('td',attrs={'class': 'table-primary'})
i = 0
while (i+2<len(data)):
  nombres.append(data[i].text)
  apellidos.append(data[i+1].text)
  especialidad.append(data[i+2].text)
  i+= 3

print(nombres)
print(apellidos)
print(especialidad)

df = pd.DataFrame({'Nombres':nombres,'Apellidos':apellidos,'Especialidad':especialidad})
df.to_csv('pacientes.csv',index = False, encoding = 'utf-8')