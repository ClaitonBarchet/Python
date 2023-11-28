print("CÁLCULO DE MÉDIA PONDERADA")
m1=float(input("Informe o peso da primeira nota: "))
m2=float(input("Informe o peso da segunda nota: "))
vn1=False
vn2=False


while vn1 == False:

    n1=float(input("Informe a primeira nota: "))

    if n1 < 0 or n1 >10:

        print("informe um numero entre 0 e 10.")

    else:

        vn1 = True



while vn2 == False:
    
    n2=float(input("Informe a segunda nota: "))

    if n2 < 0 or n2 >10:

        print("informe um numero entre 0 e 10.")

    else:

        vn2 = True

            

print("a média é: ",(m1*n1+m2*n2)/(m1+m2))

print("fim do programa")

input("Aperte ENTER para sair")
