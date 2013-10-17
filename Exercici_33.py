print "Benvingut al meu programa."
print
num = int(raw_input("Escriu el numero que representara la base de la potencia: "))
exp = int(raw_input("Escriu el exponent: "))
pot = 1

while exp >= 1:
	pot = pot*num
	exp = exp - 1

	
print "El resultat es: " + str(pot)
print "Gracies per utilitzar el meu programa"
print "Adeu"