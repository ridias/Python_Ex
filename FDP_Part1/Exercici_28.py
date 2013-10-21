print "Benvingut al meu programa"
print
hores = int(raw_input("Escriu el nombre d'hores treballades: "))

he = 0
hse = 0

if hores >= 40:
	ho = hores
elif (hores <= 60) and (hores >= 40):
	ho = 40
	he = hores - 40
else:
	ho = 40
	he = 20
	hse = hores-60
	

salari = (ho*18) + (he*30) + (hse*50)
print "El salari setmana es de: " + str(salari)
print "Gracies per utilitzar el meu programa"
print "Adeu!"