print "Benvingut al meu programa"
print 

digit = int(raw_input("Escriu el digit: "))
comptador = 0

while 0 != digit:
	examinar = digit % 2
	if examinar == 0:
		comptador = comptador + 1
	
	digit = int(raw_input("Escriu el seguent digit: "))

print "Hi ha " + str(comptador) + " numeros parells."
print
print "Gracies per la utilitzacio del meu programa"
print "Adeu!"