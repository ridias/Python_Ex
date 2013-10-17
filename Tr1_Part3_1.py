print "Benvingut al meu programa"
print
x = int(raw_input("Escriu el valor de x: "))
y = int(raw_input("Escriu el valor de y: "))
z = int(raw_input("Escriu el valor de z: "))
comptador = 0
suma = 0
para = False

while (x != -99) and (para == False):
	volum = x*y*z
	comptador = comptador + 1
	suma = suma + volum
	x = int(raw_input("Escriu el seguent valor de x: "))
	if x == -99:
		para = True
	else:
		y = int(raw_input("Escriu el seguent valor de y: "))
		z = int(raw_input("Escriu el seguent valor de z: "))
		
resultat = suma / comptador
print "Resultat: " + str(resultat)
print "Suma: " + str(suma)
print "Quants: " + str(comptador)
print
print "Gracies per utilitzar el meu programa"
print "Adeu"