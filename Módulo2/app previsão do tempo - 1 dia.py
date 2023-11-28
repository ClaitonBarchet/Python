import requests
import json
import pprint

accuweatherAPIkey = "GjF9BEiy6rmdjlusvOdOI0uk5l7YO0q0"
#accuweatherAPIkey = ""

def pegarCoordenadas():


    r = requests.get('http://www.geoplugin.net/json.gp')

    if (r.status_code!= 200):
        print('Não foi possível obter a localização.')
        return None
    else:
        try:
            ##print("r.text")
            ##print(type(json.loads(r.text))) ##IMPRIME CODIGO
            localizacao = json.loads(r.text) ##IMPRIME O CODIGO CONVERTIDO EM LISTA PYTHON  
            coordenadas={}
            coordenadas['lat'] = localizacao['geoplugin_latitude']
            coordenadas['long'] = localizacao['geoplugin_longitude']
            return coordenadas
        except:
            return None
        
def pegarCodigoLocal(lat,long):
    
        ##print('lat: ',lat)
        ##print('long: ',long)
    
        ##print(pprint.pprint(localizacao))

        ##LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/" \
                         ##+ "geoposition/search?apikey=" + accuweatherAPIkey \
                         ##+ "&q=" + lat + "%2C%" + long + "&language=pt-br"

    LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/" \
                    + "geoposition/search?apikey=" + accuweatherAPIkey + "&q=" + lat + "%2C%20" + long + "&language=pt-br"

    r = requests.get(LocationAPIUrl)
    if (r.status_code!= 200):
        print('Não foi possível obter o código do local.')
        return None
    else:
        try:
            
            ##print(pprint.pprint(json.loads(r2.text))) ##IMPRIME O CODIGO CONVERTIDO EM LISTA PYTHON

            locationResponse = json.loads(r.text)
            infoLocal = {}
            
            infoLocal['nomeLocal'] = locationResponse['LocalizedName'] + ", " \
                        + locationResponse['AdministrativeArea']['LocalizedName'] + ". " \
                        + locationResponse['Country']['LocalizedName']
            infoLocal['codigoLocal'] = locationResponse['Key']
            ##print("Local: ", nomeLocal)
            ##print("Código do local: ", codigoLocal)
            return infoLocal
        except:
            return None

def pegarTempoAgora(codigoLocal,nomeLocal):      

    ##print("Obtendo clima do local: ", nomeLocal)

    CurrentCondittionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" \
                               + codigoLocal + "?apikey=" + accuweatherAPIkey + "&language=pt-br"

    r = requests.get((CurrentCondittionsAPIUrl))
    
    if (r.status_code!= 200):
        print('Não foi possível obter clima atual.')
        return None
    else:
        try:
            CurrentConditionsResponse = json.loads(r.text)

            infoClima={}
            print(pprint.pprint(CurrentConditionsResponse))
            infoClima['textoClima'] = CurrentConditionsResponse[0]["WeatherText"]
            infoClima['temperatura'] = CurrentConditionsResponse[0]["Temperature"]["Metric"]["Value"]
            infoClima['nomeLocal'] = nomeLocal
            return infoClima
        
            ##print("Clima no momento: ",textoclima)
            ##print("Temperatura: "+ str(temperatura)+ " graus Celsius.")
        except:
            return None
    

## Início do programa


try:
    coordenadas = pegarCoordenadas()
    local = pegarCodigoLocal(coordenadas['lat'],coordenadas['long'])
    climaAtual = pegarTempoAgora(local['codigoLocal'],local['nomeLocal'])

    print('Clima atual em: ' + climaAtual['nomeLocal'])
    print(climaAtual['textoClima'])
    print('Temperatura: ' + str(climaAtual['temperatura'])+ "\xb0" + "C")

except:
    print("Erro ao processar a solicitação. entre em contato com o suporte.")
