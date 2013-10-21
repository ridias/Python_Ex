print "Benvingut al meu programa"
print
x = int(raw_input("Escriu un valor x: "))
y = int(raw_input("Escriu un valor y: "))
z = int(raw_input("Escriu un valor z: "))

numSeq = 0
comptador = 0
suma = 0
fi = False
seguent = False

while (x != 0) and (numSeq <= 200) and (fi == False):
	while (x != -99) and (seguent == False):
		volum = x*y*z
		comptador = comptador + 1
		suma = suma + volum
		x = int(raw_input("Escriu el valor seguent de x: "))
		if (x == -99) or (x == 0):
			seguent = True
		else:
			y = int(raw_input("Escriu el valor seguent de y: "))
			z = int(raw_input("Escriu el valor seguent de z: "))
	
	resultat = suma / comptador
	suma = 0
	comptador = 0
	seguent = False
	numSeq = numSeq + 1
	print "Mitjana: " + str(resultat)
	if x == 0:
		fi = True
	else:
		x = int(raw_input("Escriu el valor seguent x: "))
		y = int(raw_input("Escriu el valor seguent y: "))
		z = int(raw_input("Escriu el valor seguent z: "))
		
print "Numero de sequencies que s'han tractat: " + str(numSeq)
print
print "Gracies per utilitzar el meu programa"
print "Adeu"