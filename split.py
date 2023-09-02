print("ingresar una serie de numeros separados por espacios")
nun=input(" : ")
lista =nun.split()

for i in range(len(lista)):
    lista[i]= int (lista[i])

print(lista)
lista.sort()
print(lista)
