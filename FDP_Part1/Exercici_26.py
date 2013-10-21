print "Benvingut al meu programa"
print
any = int(raw_input("Introdueix l'any: "))


if any % 4 == 0:
	if any % 100 == 0:
		mc = any % 100
		if mc % 4 == 0:
			print "El numero es bixest."
		else:
			print "El numero no es bixest."
	else:
		print "El numero es bixest"
else:
	print "El numero no es bixest"
	
