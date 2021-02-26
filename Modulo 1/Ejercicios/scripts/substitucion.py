abecedario=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# sustitucion=["N","Q","X","P","O","M","A","F","T","R","H","L","Z","G","E","C","Y","J","I","U","W","S","K","D","V","B"]
sustitucion="NQXPOMAFTRHLZGECYJIUWSKDVB"

plaintext=input("Ingrese palabra: ")

plaintext=plaintext.upper()

nueva_palabra=''
for i in range(len(plaintext)):
    for j in range(len(abecedario)):
        if plaintext[i]==abecedario[j]:
            new_position=j
            for l in range(len(sustitucion)):
                if new_position==l:
                    nuevo=sustitucion[l]
                    nueva_palabra=nueva_palabra+nuevo
print(nueva_palabra)


            


