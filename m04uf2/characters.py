#!/usr/bin/python3

#Libreria para interpretar XML con Python
from bs4 import BeautifulSoup

#Abro el archivo XML en modo lectura
file = open('characters.facx', 'r')

#Parseo el XML
soup = BeautifulSoup(file, 'xml')

#Encuentro los personajes
characters = soup.find_all("character")

#Cierro el archivo
file.close()

title = "Bienvenido a Fary Adventures"

print(title)
print('-'*len(title))

#Pregunto accion
print("\nElije la accion:\n")
print("1- Elegir personaje\n")
print("2- Matar personaje\n")

accion = input("\nIntroduce un numero: ")

if accion == '1':
	##Elegir personaje

	print("\nElije personaje:\n")

	#Muestro los personajes que hay
	for character in characters:
		print(f"{character['id']}\t {character.find('name').text}")

	encontrado = False

	#Compruebo que exista el personaje
	while not encontrado:
		id = input("\nIntroduce un numero: ")

		file = open('characters.facx', 'r')

		soup = BeautifulSoup(file, 'xml')

		file.close()

		character = soup.find('character', {'id': id})

		if not character:
			print("Error: 	No encontrado")
		else:
			encontrado = True
		
	print("\nEl personaje seleccionado es:\n")
	print(f"\tNombre: {character.find('name').text}")
	print(f"\tEdad: {character.find('age').text}")
	print(f"\tGenero: {character.find('gender')['value']}")
	print(f"\tNivel: {character.find('level')['value']}")


	file = open('characters_weapons.facwx', 'r')

	soup = BeautifulSoup(file, 'xml')
	
	file.close()

	characters_weapons = soup.find_all('character_weapon')

	weapons_ids = []

	for character_weapon in characters_weapons:
		id_character = character_weapon.find("character")["id"]
		if id_character == id:
			id_weapon = character_weapon.find("weapon")["id"]
			weapons_ids.append(id_weapon)


	if len(weapons_ids) <= 0:
		print("El personaje no tiene armas")
		exit()

	file = open('weapons.fawx', 'r')

	soup = BeautifulSoup(file, 'xml')

	file.close()

	weapons = soup.find_all('weapon', {'id':True})


	damage = 0

	for weapon in weapons:
		if weapon['id'] in weapons_ids:
			damage = damage + int(weapon.find('damage')['value'])
	

	print(f"\tDaño: {damage}")

elif accion == '2':
	##Matar personaje
	
	print("\nMatar personaje:\n")

	#Muestro los personajes
	for character in characters:
		print(f"{character['id']}\t {character.find('name').text}")

	encontrado = False

	#Comrpuebo que existe
	while not encontrado:
		id = input("\nIntroduce un numero: ")

		file = open('characters.facx', 'r')

		soup = BeautifulSoup(file, 'xml')

		file.close()

		character = soup.find('character', {'id' : id})

		if not character:
			print("Error: No encontrado")
		else:
			encontrado = True

	#Elimino el personaje
	character.decompose()

	#Abro el archivo en modo escritura
	file = open('characters.facx', 'w')

	#Escribo la array sin el personaje eliminado
	file.write(str(soup))

	#Cierro el archivo
	file.close()




