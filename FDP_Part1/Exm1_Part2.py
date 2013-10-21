print "Benvingut al meu programa"
print

digit = int(raw_input("Escriu el digit que es tractara: "))
comptador = 0
volta = 1
primerComptador = 0
fi = False

while digit != -1 and fi == False:
	while digit != 0:
		if volta == 1:
			primerComptador = primerComptador + 1
		else:
			comptador = comptador + 1
			
		digit = int(raw_input("Escriu el seguent digit que es tractara: "))
		if digit == -1:
			fi = True
	
	if comptador == primerComptador:
		print "El numero de linea: " + str(volta)
		comptador = 0
	elif fi == False:
		digit = int(raw_input("Escriu el digit que es tractara: "))
		comptador = 0
		volta = volta + 1
	
		
		
print 
print "Gracies per utilitzar el meu programa"
print "Adeu"