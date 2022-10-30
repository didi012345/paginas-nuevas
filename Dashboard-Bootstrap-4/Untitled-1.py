def s(a, b):
    return a + b
def m(a, b):
    return a * b
def r(a, b):
    return a - b

while True:
     print("Menu principal")
     print("1. suma")
     print("2. multiplicación")
     print("3. resta")
opc = input("Ingrese una opción")
n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
if opc=="1":
        print("la suma es: ",s(n1, n2))
elif opc=="2":
        print("resta da: ",r(n1, n2))
elif opc=="3":
        print("la multiplicación da: ",m(n1, n2))
else:
        print("opción inválida")
