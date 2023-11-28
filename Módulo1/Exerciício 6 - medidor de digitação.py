print("##### MEDIDOR DE DIGITAÇÃO #####")
print("Esse programa mede o tempo que você leva para digitar uma palavra, digite a mesma palavra 5 vezes para realizar a medição.")
input("Para começar aperte ENTER...")

import time
import matplotlib.pyplot as plt

lista1=[]
lista2=[]
legenda=[]

contador = 0
inicio = 0
fim = 0
tempo = 0
palavra=0
legenda = ["1ª vez","2ª vez","3ª vez","4ª vez","5ª vez"]

while contador <5:

    inicio = time.process_time()
    ##inicio = time.process_time()

    input("Digite uma palavra: ")

    palavra = palavra + 1

    fim = time.perf_counter()
    ##fim = time.process_time()
    
    contador = contador +1

    tempo = round(fim - inicio)

    lista1.append(palavra)
    lista2.append(tempo)
    

plt.plot(lista1,lista2)

plt.xticks(lista1,legenda)

print("Tempo total: ", tempo," segundos.")

plt.show()
