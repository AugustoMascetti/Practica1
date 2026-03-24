import random
words = [
"python",
"programa",
"variable",
"funcion",
"bucle",
"cadena",
"entero",
"lista",
]

guessed = []
attempts = 6
points = 0

word = random.choice(words)



print("¡Bienvenido al Ahorcado!")
print()


while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
	progress = ""
	for letter in word:
		if letter in guessed:
			progress += letter + " "
		else:
			progress += "_ "
	print(progress)
	
# Verificar si el jugador ya adivinó la palabra completa
	if "_" not in progress:
		print("¡Ganaste!")
		points += 6
		print (f" El puntaje es: {points}")
		break
		
	print(f"Intentos restantes: {attempts}")
	print(f"Letras usadas: {', '.join(guessed)}")
	
	letter = input("Ingresá una letra: ")
	letter = letter.lower()
		
	if letter in guessed:
		print("Ya usaste esa letra.")
	elif  len(letter)>1 or not letter.isalpha():
		print()
		print  ("Entrada no válida")
	elif letter in word:
		guessed.append(letter)
		print("¡Bien! Esa letra está en la palabra.")
	else:
			guessed.append(letter)
			attempts -= 1
			points -= 1
			print("Esa letra no está en la palabra.")
		
	print()
else:
	print(f"¡Perdiste! La palabra era: {word}")
	points = 0
	print (f" El puntaje es: {points}")
