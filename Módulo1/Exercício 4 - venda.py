
fatura=[] ##CRIA A LISTA
repetir="s"
total=0
valid_vlr = False

fatura.clear


while repetir == 's':

    produto=input("nome do produto: ").lower()


    while valid_vlr == False:

        valor=input("valor do produto: ")
            
        try:
            valor=float(valor)
            
            if valor <= 0:
                print("O valor precisa ser maior que zero.")
            else:
                valid_vlr = True
                
        except:
            print("formato de preço inválido. Use apenas números e separe os centavos com '.'.")


        

    total=total + valor

    fatura.append([produto,valor]) ##ADICIONA A LISTA   
    valid_vlr = False
    repetir = input("deseja adquirir mais algum produto? S ou N ").lower()


#print(fatura)##horizontal

for i in fatura:##vertical
    print(i[0],' - ',i[1])

print('TOTAL - ',total)
