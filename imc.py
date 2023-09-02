print("Buen dia, Hoy averiguara su IMC")
p = float(input("Indique su peso(kg): "))
a = float(input("Indique su altura(m): "))
imc= p/(a*a)
x= "usted tiene "
if imc<18.5:
    print(x,"bajo peso")
elif imc<=18.5 or imc<25:
    print(x,"peso normal")
elif imc<=30 or imc<30:
    print(x,"sobrepeso")
elif imc>=30:
    print(x,"obesidad")
