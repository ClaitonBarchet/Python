


print("##############################################")
print("##### CALCULO DE COBERTURA METÁLICA SHED #####")
print("##############################################")
print("\n")
print("A proposta da ferramenta é facilitar o cálculo de algumas partes de uma cobertura metálica shed, trazendo a quantidade de terças, tesouras e telhas , facilitando as atividades do projetista orçamentista.")
print("\n")

repetir = True

while repetir == True:

    ##COMPRIMENTO

    vc = False
    while vc == False:
        comprimento = input("informe o comprimento em metros da cobertura metálica: ")
        print("\n")
        try:
            comprimento = float(comprimento)
            if comprimento <=0:
                print("Comprimento inválido. Informe apenas numero maiores que zero.")
                print("\n")
            else:
                vc = True
        except:
            print("Comprimento inválido. Infome apenas numero, e utilize ponto '.' como separador decimal.")
            print("\n")



    ##LARGURA
            
    vl = False
    while vl == False:
        largura = input("informe a largura em metros da cobertura metálica: ")
        print("\n")
        try:
            largura = float(largura)
            if largura <=0:
                print("Largura inválida. Informe apenas numero maiores que zero.")
                print("\n")
            else:
                vl = True
        except:
            print("Largura inválida. Infome apenas numero, e utilize ponto '.' como separador decimal.")
            print("\n")



    ##CAIMENTOS (ÁGUAS)
            
    va = False
    while va == False:
        águas = input("Informe se a cobertura é uma água ou duas águas: (1 ou 2): ")
        print("\n")

        try:
            águas = float(águas)
            if águas <1 or águas > 2:        ##if águas != "1" or águas != "2":     <<<<----- pq essa expressão nao funciona???
                print("Quantidade de caimentos inválida.")
                print("\n")
            else:
                va = True
        except:
            print("Caimento inválido.")
            print("\n")


            

    custo_area = 90.00 ##custo por m² arbitrado.



    comp_tesoura = int(largura / águas)
    qtd_tesouras = round((comprimento / 5)+1)*(águas)
    comp_terça = round((comp_tesoura / 1.2)+1)*(comprimento)*(águas)
    area_telhas = (largura)*(comprimento)
    custo_aprox = (area_telhas)*(custo_area)
    pilares= round((comprimento/5)+1)+((largura/5)+1)



    print("Serão necessárias ", qtd_tesouras,"tesouras de ",comp_tesoura,"metros de comprimento.")

    print("Serão necessários ", comp_terça," metros de terçamento.")

    print("Serão necessários ", pilares," pilares.")

    print("Serão necessários ", area_telhas," metros quadrados de telha.")

    print("Custo aproximado para confecção: ","R$ ",custo_aprox)
    print("\n")

    

    ##CHECA REPETIÇÃO

    vr = False

    while vr == False:
        insp = input("Aperte s para sair do programa ou r para repetir .").lower()

        if insp != "s" and insp != "r":
            print("Opção inválida.")
        else:
            vr = True



    if insp == "s":

        repetir = False

    else:
        repetir = True
        print("\n")
        
print("\n")
input("Fim da programação aperte ENTER.")

