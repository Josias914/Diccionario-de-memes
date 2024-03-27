meme_dict = {
    "LOL" : "Una respuesta a algo gracioso",
    "CRINGE" : "Algo raro o embarazoso",
    "ROFL" : "Una respuesta a una broma",
    "SHEESH" : "Ligera desaprobación",
    "CREEPY" : "Aterrador, siniestro",
    "AGGRO" : "Ponerse agresivo/enojado"
}

saludo = input("Bienvenido al diccionario(pulsa enter para continuar) ")

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!):")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("por ahora no yo tampoco se cual es esa palabra")

print("Gracias por usar el diccionario vuelve pronto")
