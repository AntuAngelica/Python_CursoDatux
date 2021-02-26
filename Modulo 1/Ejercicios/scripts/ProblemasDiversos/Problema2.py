import math
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))

discriminante=(b**2)-(4*a*c)

if discriminante>0:
    x1=(-b+math.sqrt(discriminante)/2*a)
    x2=(-b-math.sqrt(discriminante)/2*a)
    print(x1," ",x2)

elif discriminante==0:
    x=-b/(2*a)
    print(x)

else:
    print("No tiene solucion real")