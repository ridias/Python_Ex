print "Benvingut al meu programa"
print
x = int(raw_input("Escriu un valor x: "))
y = int(raw_input("Escriu un valor y: "))
z = int(raw_input("Escriu un valor z: "))

maxim = -1
numSeq = 0
fi = False
seguent = False
trobat = False

while (x != 0) and (numSeq <= 200) and (fi == False):
	while (x != -99) and (seguent == False) and (trobat == False):
		volum = x*y*z
		if (numSeq == 0) and (maxim < volum):
			maxim = volum
			print "Maxim es: " + str(maxim)
		elif maxim == volum:
			seguent = True
			trobat = True
			print "S'ha trobat un volum igual al maxim del primer poligon industrial i pot haver-hi mes"
		
		if trobat == False:
			x = int(raw_input("Escriu el seguent valor x: "))
			if (x == -99) or (x == 0):
				seguent = True
			else:
				y = int(raw_input("Escriu el seguent valor y: "))
				z = int(raw_input("Escriu el seguent valor z: "))
	
	seguent = False
	numSeq = numSeq + 1
	if (x == 0) or (trobat == True):
		fi = True
	else:
		x = int(raw_input("Escriu el seguent valor x: "))
		y = int(raw_input("Escriu el seguent valor y: "))
		z = int(raw_input("Escriu el seguent valor z: "))
		
print "Numero de sequencies que s'han tractat: " + str(numSeq)
print
print "Gracies per utilitzar el meu programa"
print "Adeu"