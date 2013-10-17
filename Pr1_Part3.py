print "Benvingut al meu programa"
print
num = int(raw_input("Escriu una altura: "))

sumAltura = 0
comptador = 0
quantsMaxim = 0
quantsMinim = 1
resultat = 0
minValor = num

while num != -999:
	sumAltura = sumAltura + num
	comptador = comptador + 1
	if minValor = num:
		quantsMinim = quantsMinim + 1
		
	if (num < minValor) and (num > 0):
		minValor = num
		print "El valor es: " + str(minValor)
		quantsMinim = 1
	
	if num >= 2600:
		quantsMaxim = quantsMaxim + 1
	
	num = int(raw_input("Escriu la seguent altura: "))

if quantsMaxim >= 1:
	print "En la sequencia existeix com a minim un valor superior a 2600"
else:
	print "No existeix cap valor superior a 2600 en la sequencia"
	

resultat = sumAltura / comptador
print "Suma dels valors: " + str(sumAltura)
print "Numero de valors introduits: " + str(comptador)
print "La mitjana dels valors de la sequencia es de: " + str(resultat)
print "El valor mes baix de la sequencia es: " + str(minValor)
print "Numero de vegades que apareix el mateix valor mes baix de la sequencia: " + str(quantsMinim) + " cops."
print
print
print "Gracies per utilitzar el meu programa"
print "Adeu" 