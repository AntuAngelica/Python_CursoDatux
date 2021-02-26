n=int(input("Ingrese cantidad de lineas: "))
while n<=0:
    n=int(input("Vuelva a ingresar, numero invalido: "))
for i in range(n+1):
    blanco=n-i
    print(' '*blanco+'#'*i)

