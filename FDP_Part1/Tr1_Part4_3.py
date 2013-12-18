print "Benvingut al meu programa"
print
x = int(raw_input("Escriu un valor x: "))
y = int(raw_input("Escriu un valor y: "))
z = int(raw_input("Escriu un valor z: "))

igualX = x
igualY = y
igualZ = z
numSeq = 0
fi = False
comptador = 0
seguent = False
consecutiu = False

while (x != 0) and (numSeq <= 200) and (fi == False):
	while (x != - 99) and (seguent == False):
		volum = x*y*z
		if (igualX == x) and (igualY == y) and (igualZ == z):
			comptador = comptador + 1
			print "Portes: " + str(comptador)
			if comptador == 3:
				seguent = True
				consecutiu = True
		else:
			igualX = x
			igualY = y
			igualZ = z
			comptador = 1
			consecutiu = False
		
		if seguent == False:
			x = int(raw_input("Escriu el seguent valor x: "))
			if (x == -99) or (x == 0):
				seguent = True
				comptador = 0
			else:
				y = int(raw_input("Escriu el seguent valor y: "))
				z = int(raw_input("Escriu el seguent valor z: "))
	
	seguent = False
	numSeq = numSeq + 1
	if (x == 0) or (consecutiu == True):
		fi = True
	else:
		x = int(raw_input("Escriu el seguent valor x: "))
		y = int(raw_input("Escriu el seguent valor y: "))
		z = int(raw_input("Escriu el seguent valor z: "))
		
if consecutiu == True:
	print "S'ha trobat com a minim el mateix volum amb les mateixes mesures"
else:
	print "No s'ha trobat cap"
	
print "Numero de sequencies que s'han tractat: " + str(numSeq)
print
print "Gracies per utilitzar el meu programa"
print "Adeu"
	
			