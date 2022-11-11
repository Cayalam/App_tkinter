print("-----------------------")
print("-INVERTIR-LOS-NÚMEROS-")
print("-----------------------")

n =input("Digite un número de cuatro cifras ")
n = int(n)
x = "Error, inténtelo de nuevo"

n4 = n % 10
n3 = (n % 100)//10
n2 = (n % 1000)//100
n1 = (n-(n % 1000))//1000
print("El número inverso es: "+ str(n4) + str(n3) + str(n2) + str(n1) )