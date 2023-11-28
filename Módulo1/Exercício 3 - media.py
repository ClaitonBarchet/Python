nome = input("nome: ").lower()
vn1 = False
vn2 = False
vf = False

while vn1 == False:

    nota1 = input("nota da primeira prova: ")

    try:
        nota1 = float(nota1)


        if nota1 < 0 or nota1 > 10:
            print("Informe um numero entre 0 e 10.")
        else:
            vn1 = True


    except:
        print("Formato não suportado informe um numero e separe as casas por ponto.")



        
        
while vn2 == False:

    nota2 = input("nota da segunda prova: ")

    try:
        nota2 = float(nota2)

        if nota2 <0 or nota2 >10:
            print("informe um numero entre 0 e 10.")
        else:
            vn2 = True

    except:
        print("Formato não suportado informe um numero e separe as casas por ponto.")

        

while vf == False:
    
    faltas = input("quantidade de faltas: ")

    try:
        faltas = float(faltas)

        if faltas < 0 or faltas >20:
            print("Informe a quantidade de faltas entre 0 à 20.")
        else:
            vf = True

    except:
        print("Formato não suportado informe um numero e separe as casas por ponto.")
        



media = (nota1 + nota2)/2
assid = ((20 - faltas)/20)*100

if faltas > 14 and media < 6:

    print("reprovado por média e faltas")         

elif faltas > 14:

    print("reprovado por faltas")

elif media < 6:

    print("reprovado por média")
        
else:
    print(nome)
    print(media)
    print(assid, "%")
    print("APROVADO")
