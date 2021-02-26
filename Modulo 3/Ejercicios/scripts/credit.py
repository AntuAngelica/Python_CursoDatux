suma=0
suma_1=0
total=0
num="4111111111111111"
nombre=''
for i in range(len(num)-2,-1,-2):
    multi=int(num[i])*2
    multi=str(multi)
    for j in range(len(multi)):
        suma=suma+int(multi[j])
for m in range(len(num)-1,-1,-2):
    suma_1=suma_1+int(num[m])
total=suma_1+suma

if total % 10 == 0:
    print("La tarjeta es legítima")

    if len(num)==15:
        for l in range(0,2):
            if num[0]=='3':
                if num[1]=='7' or num[1]=='4':
                    nombre='AMEX'
    elif len(num)==16:
        for o in range(0,2):
            if num[0]=='5':
                nu=int(num[1])
                if nu in range(0,6):
                    nombre='MASTERCARD'
            elif num[0]=='4':
                nombre='VISA'
    elif len(num)==13:
        for p in range(0,1):
            if num[0]=='4':
                nombre='VISA'

    print(nombre)
else:
    print("INVALID")

