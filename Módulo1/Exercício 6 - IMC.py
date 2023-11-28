print("#####CÁLCULO IMC#####")

vs = False

while vs == False:
    sexo = input("Informe seu sexo.(M ou F) ").lower()

    if sexo != 'm' and sexo != 'f':
        print("Sexo inválido. Digite m ou f.")
    else:
        vs = True



vp = False

while vp == False:
    peso = input("Informe seu peso. (para separar casas decimais utilize ponto '.' ")

    try:
        peso = float(peso)

        if peso <= 0 or peso > 350:
            print("Peso inválido! não pode ser zero ou negativo ou superior a 350")
        else:
            vp = True

    except:
        print("Peso inválido. use apenas numeros e separe os decimais com ponto '.'.")



va = False

while va == False:
    
    altura = input("Informe sua altura, para separar casas decimais utilize ponto '.' ")

    try:
        altura = float(altura)

        if altura <= 0 or altura > 3:
            print("Altura inválida! valor ão pode ser zero ou negativo ou superior a 3")
        else:
            va = True

    except:
        print("altura inválida. use apenas numeros e separe os decimais com ponto '.'.")



imc = peso / (altura * altura)


def mgs1():
    print("Abaixo do peso.")

def mgs2(mgs2):
    print("No peso normal.")

def mgs3():
    print("Marginalmente acima do peso.")

def mgs4():
    print("Acima do peso ideal.")

def mgs5():
    print("Obeso.")



if sexo == "f":

            if imc < 19.1:

                ##msg1()

                print("Abaixo do peso.")

            elif imc > 19.1 and imc < 25.8:

                ##msg2()

                print("No peso normal.")

            elif imc > 25.8 and imc < 27.3:

                ##msg3()

                print("Marginalmente acima do peso.")

            elif imc > 27.3 and imc < 32.3:

                ##msg4()

                print("Acima do peso ideal.")

            elif imc > 32.3:

                ##msg5()

                print("Obeso.")

                

elif sexo == "m":

            if imc < 20.7:

                ##msg1()

                print("Abaixo do peso.")

            elif imc > 20.7 and imc < 26.4:

                ##msg2()

                print("No peso normal.")

            elif imc > 26.4 and imc < 27.8:

                ##msg3()

                print("Marginalmente acima do peso.")

            elif imc > 27.8 and imc < 31.1:

                ##msg4()

                print("Acima do peso ideal.")

            elif imc > 31.1:

                ##msg5()

                print("Obeso.")
                
input("Aperte ENTER para sair.")
    

