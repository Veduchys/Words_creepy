palabra = input("¿Qué palabras conoces?)
meme_dict = ("Patidifuso": "Sorprendido,
"cringe":"vergonsoso,pena ajena",
"GG":"good game",
"momos":"imagenes graciosas",
"IDK": "i don´t know/no sé",
"WDYM":"What do you mean/a que te refieres",
"WTH":"What the hell/que demonios?",
"HBD":"Happy birthday",
"XD":"cara de risa",
"Noob":"novato,principiante")

if palabras in meme_dict.keys():
  print(meme_dict[palabra])
else:
  print("Esa palabra no esta el la lista!")
