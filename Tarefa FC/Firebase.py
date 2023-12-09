#BANCO
def FBanco():
    import json
    import pyrebase
    from pyrebase import pyrebase
    from firebase_admin import db
    import firebase_admin

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

#ABRE O JSON
    #with open("lista.json", "r") as f:
        #dados = json.load(f)
        #ref.set(dados)
        #print(dados)
    #ref.push(dados)

    firebase = pyrebase.initialize_app(config)

    dados = firebase.database()

    
    
    #teste
    #Bdados = {"time" : "internacional", "Ponto" : 90}
    #print (Bdados)
    #
    #for i in dados:
        
        #dados.child().update({i : i})
    dados.child().update({"nome" : "claiton" })
    dados.child().update({"idade" : 35})
        #dados.child().update({lista.json})

print("Firebase, OK!")