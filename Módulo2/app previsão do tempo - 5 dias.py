import requests
import json
import pprint
from datetime import date

accuweatherAPIkey = "GjF9BEiy6rmdjlusvOdOI0uk5l7YO0q0"
##accuweatherAPIkey = ""

dias_semana = ['Domingo','Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira','Sábado']

def pegarCoordenadas():
    r = requests.get('http://www.geoplugin.net/json.gp')

    if (r.status_code!= 200):
        print('Não foi possível obter a localização.')
        return None
    else:
        try:

            localizacao = json.loads(r.text) ##IMPRIME O CODIGO CONVERTIDO EM LISTA PYTHON  
            coordenadas={}
            coordenadas['lat'] = localizacao['geoplugin_latitude']
            coordenadas['long'] = localizacao['geoplugin_longitude']
            return coordenadas
        except:
            return None
        
def pegarCodigoLocal(lat,long): ######## ALGUM ERRO AQUI, site nao fornecendo informação 503.
    LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/" \
                     + "search?apikey=" + accuweatherAPIkey \
                    + "&q=" + lat + "%2C" + long + "&language=pt-br"


    r = requests.get(LocationAPIUrl)

    if (r.status_code!= 200):
        print('Não foi possível obter o código do local.')
        return None
    else:
        #try:

        locationResponse = json.loads(r.text)
        infoLocal = {}
        infoLocal['nomeLocal'] = locationResponse['LocalizedName'] + ", " \
                        + locationResponse['AdministrativeArea']['LocalizedName'] + ". " \
                        + locationResponse['Country']['LocalizedName']
        infoLocal['codigoLocal'] = locationResponse['Key']
        return infoLocal
        #except:
            #return None



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



        
def pegarPrevisao5Dias(codigoLocal):
    
    DailyAPIUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" \
                               + codigoLocal + "?apikey=" + accuweatherAPIkey + "&language=pt-br&metric=true"


    r = requests.get((CurrentCondittionsAPIUrl))
    
    if (r.status_code!= 200):
        print('Não foi possível obter clima atual.')
        return None
    else:
        try:
            DailyResponse = json.loads(r.text)
            infoClima5Dias = []
            
            for dia in DailyResponse['DailyForecasts']:
                climaDia = {}
                climaDia['max'] = dia['Temperature']['Maximum']['Value']
                climaDia['min'] = dia['Temperature']['Minimum']['Value']
                climaDia['clima'] = dia['Day']['IconPhrase']
                diaSemana = int(date.fromtimestamp(dia['EpochDate']).strftime("%w"))
                climaDia['dia'] = dias_semana[diaSemana]
                infoClima5Dias.append(climaDia)
            return infoClima5Dias  
                
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

    print("\nclima para hoje e para os próximos dias: \n")

    previsao5Dias = pegarPrevisao5Dias(local['codigoLocal'])

    for dia in previsao5dias:
        print(dia[dia])
        print('Mínima: ' + str(dia['min']) + "\xb0" + "C")
        print('Máxima: ' + str(dia['max']) + "\xb0" + "C")
        print('Clima: ' + dia['clima'])
        print("------------------------------------------")
    print(previsao5Dias)



except:
    print("Erro ao processar a solicitação. entre em contato com o suporte.")
