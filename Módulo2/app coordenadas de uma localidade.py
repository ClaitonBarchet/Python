
print('#####################################')
print('### COORDENADAS DE UMA LOCALIDADE ###')
print('#####################################')

import requests #biblioteca para chamada de função
import urllib.parse #biblioteca para troca de caracteres "Los%20Angeles" o espaço esta como %20.
import pprint #biblioteca para converter codigo
import json #biblioteca java

APIkey = "pk.eyJ1IjoiY2JhcmNoZXQiLCJhIjoiY2s2NnI1OGhwMTI4MzNycDl2a2ljdnZ0dyJ9._lJ4P8ScS6iPutjHjtSQ_Q"

def pesquisarLocal(local):
    _local = urllib.parse.quote(local)
    print(_local)
    mapboxGeocodeUrl = "https://api.mapbox.com/geocoding/v5/mapbox.places/" \
                       + _local +".json?access_token=" + APIkey #"pk.eyJ1IjoiY2JhcmNoZXQiLCJhIjoiY2s2NnF6NHhsMW9ocjNlb2Ztejc5aGxzaSJ9.BTk1S1WA2tQIJICzlrIoVw"
    r = requests.get(mapboxGeocodeUrl)
    if(r.status_code != 200):
        print("Não foi possível obter o clima atual.")
        return None
    else:
        try:
            MapboxResponse = json.loads(r.text)
            #coordenadas = {}
            #coordenadas['long'] = str(MapboxResponse['features'][0]['geometry']['coordinates'][0])
            #coordenadas['lat'] = str(MapboxResponse['features'][0]['geometry']['coordinates'][1])
            #return coordenadas
            print(pprint.pprint(MapboxResponse))
        except:
            print("Erro de pesquisa!")

cidade = input("Informe a cidade: ")


try:
    pesquisarLocal(cidade)
    print(coordenadas)
except:
    print("Erro de pesquisa!")


