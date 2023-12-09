#SCRAPING
from requests_html import HTMLSession
import unidecode

#import pyrebase
from pyrebase import pyrebase
from firebase_admin import db
config = {
        'apiKey': "AIzaSyCl8oAMpTdus1SrL_7VhUIV-vS9310MgOE",
        'authDomain': "fconsults-86df2.firebaseapp.com",
        'projectId': "fconsults-86df2",
        'storageBucket': "fconsults-86df2.appspot.com",
        'messagingSenderId': "1036175121879",
        'appId': "1:1036175121879:web:c34b9d67cf2e1fa2523f92",
        'measurementId': "G-82ZH3NY2DS",
        'databaseURL' : "https://fconsults-86df2-default-rtdb.firebaseio.com/"
    }

firebase = pyrebase.initialize_app(config)
dados = firebase.database()
session = HTMLSession()

print("Acessando WEB! Aguarde...")

url = session.get("https://www.tabeladobrasileirao.net/")
nome_times = url.html.find(".club-name--desktop")
pontos = url.html.find(".points")

#ADICIONA INFORMAÇÃO AO BANCO
print("Varrendo e salvando dados! Aguarde...")
for i in range(20):

    time = nome_times[i].text
    ponto = pontos[i + 1].text

    nome = unidecode.unidecode(time)

    dados.child(i).update({"time" : nome })
    dados.child(i).update({"pontos" : ponto })

#print(dicionario)
print("Scraping, OK!!! Concluído!")