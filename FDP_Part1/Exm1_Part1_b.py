print "Benvingut al meu programa"
print 

digit = int(raw_input("Escriu el digit que es tractara: "))
ok = False
socPrimer = False

while (digit != 0) and (ok == False):
	if digit == 3:
		socPrimer = True
		digit = int(raw_input("Escriu el seguent digit que es tractara: "))
	elif (digit == 7) and (socPrimer == True):
			ok = True 
	else:
		digit = int(raw_input("Escriu el seguent digit que es tractara: "))

if ok == True:
	print "El numero 3 esta abans o precedeix de 7"
else:
	print "No hi ha cap 3 que precedeixi o que estigui abans de 7"
	
print 
print "Gracies per utilitzar el meu programa"
print "Adeu"