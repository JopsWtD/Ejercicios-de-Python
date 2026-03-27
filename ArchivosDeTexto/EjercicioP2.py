print("Digite un texto para contar cuantas veces aparece cada palabra en él.")
texto = input("")

with open("texto.txt","w", encoding="utf-8") as file:
    file.write(texto)

with open("texto.txt", "r", encoding="utf-8") as file:
    texto = file.read().lower()
    for caracter in texto:
        if caracter not in "abcdefghijklmnñopqrstuvwxyzáéíóú ":
            texto = texto.replace(caracter,"")

palabras = texto.split()

conteo = {}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1


listaOrdenada = sorted(conteo.items(), key=lambda x: x[1], reverse=True)

print("Las palabras más repetidas son: ")
for i in range (0,min(5,len(listaOrdenada))):
    palabra, veces = listaOrdenada[i]
    print(f"La palabra \"{palabra.title()}\" se repite {veces} veces.")
