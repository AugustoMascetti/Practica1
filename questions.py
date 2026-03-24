import random

categorias ={
	"UnaVocal": ['python'],
	"DosVocales": ["lista","bucle"],
	"TresVocales": ["programa","funcion","cadena","entero"],
	"CuatroVocales": ["variable"]
}


points = 0


print("¡Bienvenido al Ahorcado!")
print()

print(""" Categorias 
	-UnaVocal
	-DosVocales
	-TresVocales
	-CuatroVocales """)
print()
	
categoria_elegida= input("Escribi una categoria(respetar mayusculas): ")


word = random.sample(categorias[categoria_elegida],len(categorias[categoria_elegida]))

for i in range (len(categorias[categoria_elegida]) ):
	print()
	attempts = 6
	guessed = []
	while attempts > 0 :
# Mostrar progreso: letras adivinadas y guiones para las que faltan
		progress = ""
		for letter in word[i]:
			if letter in guessed:
				progress += letter + " "
			else:
				progress += "_ "
		print(progress)
	
# Verificar si el jugador ya adivinó la palabra completa
		if "_" not in progress:
			print("¡Ganaste!")
			points += 6
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
		elif letter in word[i]:
			guessed.append(letter)
			print("¡Bien! Esa letra está en la palabra.")
		else:
				guessed.append(letter)
				attempts -= 1
				points -= 1
				print("Esa letra no está en la palabra.")
		
		print()
	else:
		print(f"¡Perdiste! La palabra era: {word[i]}")
		points = 0
print(f" el puntaje final es: {points}")
