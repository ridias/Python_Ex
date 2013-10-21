print "Benvingut al meu programa"
print
x = int(raw_input("Escriu el valor de x: "))
y = int(raw_input("Escriu el valor de y: "))
z = int(raw_input("Escriu el valor de z: "))
comptador = 1
maxim = -1
para = False

while (x != -99) and (para == False):
	volum = x*y*z
	if maxim == volum:
		comptador = comptador + 1
	elif maxim <= volum:
		maxim = volum
		comptador = 1
	
	x = int(raw_input("Escriu el seguent valor de x: "))
	if x == -99:
		para = True
	else:
		y = int(raw_input("Escriu el seguent valor de y: "))
		z = int(raw_input("Escriu el seguent valor de z: "))
		
print "El maxim es: " + str(maxim)
print "Numero de vegades que es repeteix el maxim: " + str(comptador) + " cops."
print
print "Gracies per utilitzar el meu programa"
print "Adeu"