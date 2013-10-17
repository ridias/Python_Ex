print "Benvingut al meu programa"
print
a = int(raw_input("Escriu el numero que s'avalua: "))

mg = a
mp = a
qmg = 1
qmp = 1

while a != 0:
	if a > mg:
		mg = a
		qmg = 1
	elif a == mg:
		qmg = qmg + 1
	
	if a < mp:
		mp = a
		qmp = 1
	elif a == mp:
		qmp = qmp + 1
		
	a = int(raw_input("Escriu el seguent numero que s'avalua: "))
	
			
print "El mes gran es: " + str(mg) + "; Frequencia: " + str(qmg)
print "El mes petit es: " + str(mp) + "; Frequencia: " + str(qmp)
print "Gracies per utilitzar el meu programa"
print "Adeu"