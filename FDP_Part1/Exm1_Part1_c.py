print "Benvingut al meu programa"
print

digit = int(raw_input("Escriu el digit que es tractara: "))
ok = True
primer = digit

while (digit != 0) and (ok == True):
	if primer <= digit:
		ok = True
		primer = digit
		digit = int(raw_input("Escriu el seguent digit que es tractara: "))
	else:
		ok = False
		
if ok == True:
	print "La sequencia esta ordenada"
else:
	print "La sequencia no esta ordenada"
	
print
print "Gracies per utilitzar el meu programa"
print "Adeu"