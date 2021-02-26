# PROBLEMA 1:
notas=[]
alumnos=[]
n=0
def ingresar_nombres():
    global n
    n=int(input("Ingrese cantidad de alumnos: "))
    for i in range(n):
        nombre=input("Ingresar nombre del alumno: ")
        nota1=int(input("Ingresar la primera nota: "))
        nota2=int(input("Ingresar la segunda nota: "))
        nota3=int(input("Ingresar la tercera nota: "))
        if nota1<0 and nota1>10:
            nota1=input("Vuelva a ingresar nota 1: ")
        if nota2<0 and nota2>10:
            nota2=input("Vuelva a ingresar nota 2: ")
        if nota3<0 and nota3>10:
            nota3=input("Vuelva a ingresar nota 3: ")
        alumnos.append(nombre)
        notas.append([nota1,nota2,nota3])

def mostrar_alumnos():
    for j in range(n):
        print(alumnos[j],notas[j][0],notas[j][1],notas[j][2])

ingresar_nombres()
mostrar_alumnos()

# PROBLEMA 2:

def aprobar_alumnos():
    alu_desaprobado=0
    alu_aprobado=0
    for j in range(n):
        suma=(notas[j][0]+notas[j][1]+notas[j][2])/3
        if suma<4:
            alu_desaprobado+=1
        elif suma>=4 and suma<=10:
            alu_aprobado+=1
    print("La cantidad de alumnos desaprobados es: ",alu_desaprobado)
    print("La cantidad de alumnos aprobados es: ",alu_aprobado)

aprobar_alumnos()

# PROBLEMA 3:

def promedio_total():
    total=0
    for j in range(n):
        promedio_unitario=(notas[j][0]+notas[j][1]+notas[j][2])/3
        total+=promedio_unitario
    promedio=total/n
    print(promedio)

promedio_total()

# PROBLEMA 4:

promedios=[]
def promedio_alto_bajo():
    for j in range(n):
        promedio=(notas[j][0]+notas[j][1]+notas[j][2])/3
        promedios.append(promedio)
    mayor=promedios[0]
    for l in range(n):
        if promedios[l]>mayor:
            mayor=promedios[l]
    print("El mayor promedio es: ",mayor)
    menor=promedios[0]
    for r in range(n):
        if promedios[r]<menor:
            menor=promedios[r]
    print("El menor promedio es: ",menor)

promedio_alto_bajo()

# PROBLEMA 5:

def buscar_alumno():
    buscar_nombre=input("Ingrese nombre a buscar: ")
    for i in range(n):
        promedio=(notas[i][0]+notas[i][1]+notas[i][2])/3
        promedios.append(promedio)
        if buscar_nombre==alumnos[i]:
            print(alumnos[i],notas[i][0],notas[i][1],notas[i][2],promedios[i])

buscar_alumno()      


