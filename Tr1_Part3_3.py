print "Benvingut al meu programa"
print
x = int(raw_input("Escriu el valor de x: "))
y = int(raw_input("Escriu el valor de y: "))
z = int(raw_input("Escriu el valor de z: "))
trobat = False
para = False

while (x != -99) and (para == False) and (trobat == False):
	volum = x*y*z
	if volum == 20:
		trobat = True
	else:
		x = int(raw_input("Escriu el seguent valor de x: "))
		if x == -99:
			para = True
		else:
			y = int(raw_input("Escriu el seguent valor de y: "))
			z = int(raw_input("Escriu el seguent valor de z: "))
  

if trobat == True:
	print "S'ha trobat com a minim un volum igual a 20"
else:
	print "No s'ha trobat cap"

	
print
print "Gracies per utilitzar el meu programa"
print "Adeu"
