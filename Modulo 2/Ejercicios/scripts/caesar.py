abecedario="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nueva=''
clave=int(input("Ingrese clave: "))

plaintext=input("Ingrese texto: ")
plaintext=plaintext.upper()

for i in range(len(plaintext)):
    for j in range(len(abecedario)):
        if plaintext[i]==abecedario[j]:
            nuevo_1=j
            nuevo_2=nuevo_1+clave
            if nuevo_2>len(abecedario):
                nuevo_2=nuevo_2%26
            nueva=nueva+abecedario[nuevo_2]

print(nueva)