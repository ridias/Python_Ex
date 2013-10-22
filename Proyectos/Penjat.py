def separar(cadena):
	lista = []
	lista.extend(cadena)
		
	return lista
		

def buscar(lista, lista2, trobat, lletra):
	pos = 0
	trobat = False
	limit = len(lista)
	while limit != 0:
		if lista[pos] == lletra:
			inserir(lista2, pos, lletra)
			limit = len(lista)
			lista[pos] = 0
			pos = 0
			trobat = True
			
		limit = limit - 1
		pos = pos + 1
	
	print limit
	return lista2, trobat
	
	
def inicializarTabla(lista, cuantos):

		for espacio in range(cuantos):
			lista.append(espacio)
			
		return lista
		
		
def inserir(lista2, pos, caracter):
	lista2[pos] = caracter
	
	return lista2	

#verifica si ha acabado el juego	
def verificar(lista, lista2):
	completo = True
	pos = 0
	x = len(lista)
	while completo == True and  x!= 0:
		if lista[pos] == 0:
			completo = True
		else:
			completo = False
			
		pos = pos + 1
		x = x - 1
		
	return completo
	

#Programa Principal
	
print "Benvingut al meu programa"
print "Aquest programa sera una simulacio del penjat"

palabras = str(raw_input("Entra la paraula que vols que la persona adivini: "))
nombrErrors = 0  #total d'errors = 12
adivinar = []
guanyat = False
ok = False


palabras = separar(palabras)
print palabras

adivinar = inicializarTabla(adivinar, len(palabras))
print adivinar
	
letra = str(raw_input("Entra la primera lletra: "))

while nombrErrors != 12 and guanyat == False:
	tupla = buscar(palabras, adivinar, ok, letra)
	if tupla[1] == True:
		print adivinar
		guanyat = verificar(palabras, adivinar)
		if guanyat == True:
			print "Has guanyat el joc, has adivinat la paraula"
		else:
			letra = str(raw_input("Entra la seguent lletra: "))
	else:
		nombrErrors = nombrErrors + 1
		letra = str(raw_input("Entra la seguent lletra: "))

palabra = ""
for caracter in adivinar:
	palabra = palabra + caracter
	
print "La paraula es: ", palabra

print "Gracies per haver jugat al joc"
print "Adeu"	