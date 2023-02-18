import string

# Crear el diccionario de cifrado
it = 0
abc = list(string.ascii_uppercase)
caesar = {i: "" for i in abc}

for i in abc:
    trileder = abc[(it + 3) % 26]
    caesar[i] += trileder
    it += 1
# Pedir al usuario un texto para cifrar
texto = input("Introduce un texto: ").upper()
# Convertir el texto utilizando el cifrado César
texto_cifrado = ""

for letra in texto:
    if letra in caesar:
        texto_cifrado += caesar[letra]
    else:
        texto_cifrado += letra

# Mostrar el texto cifrado
print("Texto cifrado:", texto_cifrado)