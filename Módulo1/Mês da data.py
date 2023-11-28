
meses = ("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")

data_nasc = input("Informe a data de nascimento no formato DD-MM-AAAA: ")


mes=int(data_nasc[3:5])-1

resp=meses[mes]


print("você nasceu no mês de ",resp)
