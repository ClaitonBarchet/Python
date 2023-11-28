n1 = 0
n2 = 0
media = 0
falta = 0

vld1 = False
vld2 = False
vld3 = False


while vld1 == False:

    n1 = float(input("informe a primeira nota. "))

    if n1 > 10 or n1 <0:
        print("Informe uma nota de 0 à 10")
    else:
        vld1 = True
        

while vld2 == False:

    n2 = float(input("informe a segunda nota. "))

    if n2 > 10 or n2 <0:
        print("Informe uma nota de 0 à 10")
    else:
        vld2 = True
        

media = (n1 + n2 )/2



while vld3 == False:

    falta = float(input("Informe a quantidade de faltas. "))

    if falta < 0 or falta >20:

        print("informe um numero de faltas entre 0 à 20.")

    else:

        vld3 = True


print("Media: ", media)
print("Faltas: ", falta)

