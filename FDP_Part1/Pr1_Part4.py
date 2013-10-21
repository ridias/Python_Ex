print "Benvingut al meu programa"
print
a = int(raw_input("Escriu el divident: "))
b = int(raw_input("Escriu el divisor: "))
comptadorDecimal = int(raw_input("Escriu el numero de decimals que vols: "))

resta = 0
decimal = 0
resultat = 0
para = False
decimalTotal = 0
aux = 0

while a > 0:
	a = a - b
	resultat = resultat + 1
	if a == 0:
		resta = 0
		print "Resultat: " + str(resultat)
		print "Resta: " + str(resta)
	elif a < b:
		resta = a
		a = 0
		comptadoResta = 0
		novaResta = 0
		print "Resultat: " + str(resultat)
		print "Resta: " + str(resta)
		while comptadoResta != 10:
			novaResta = novaResta + resta
			comptadoResta = comptadoResta + 1
		resta = novaResta
		print "Proxima resta: " + str(resta)
		

aux = 0
while comptadorDecimal != 0:	
	while (resta > (b-1)) and (para == False):
		resta = resta - b
		decimal = decimal + 1
		aux = aux + 1
		print "Resta vale: " + str(resta)
		print "Decimal vale: " + str(decimal)
		if resta == 0:
			if comptadoResta != 10:
				comptadoResta = 0
				decimalTotal = 0
				while comptadoResta != 10:
					decimalTotal = decimalTotal + decimal
					print "Nou decimal: " + str(decimalTotal)
					comptadoResta = comptadoResta + 1
				decimalTotal = decimalTotal - aux
				aux = 0
				decimal = decimalTotal
			else:	
				print "Resultat final: " + str(resultat) + "," + str(decimal)
				para = True
		elif resta < b:
			comptadoResta = 0
			novaResta = 0
			if comptadorDecimal != 1:
				decimalTotal = 0
				while comptadoResta != 10:
					novaResta = novaResta + resta
					decimalTotal = decimalTotal + decimal
					print "Seguent Resta: " + str(novaResta)
					print "Seguent total decimal: " + str(decimalTotal)
					comptadoResta = comptadoResta + 1
			else:
				decimalTotal = decimal
		print "Total del total: " + str(decimalTotal)
	if para == False:
		resta = novaResta
		decimal = decimalTotal
	comptadorDecimal = comptadorDecimal - 1
	

print "Resultado final del final: " + str(resultat) + "," + str(decimal)
print
print "Gracies per utilitzar el meu programa"
print "Adeu"
					