print "Benvingut al meu programa"
print 

n = int(raw_input("Escriu el numero a tractar: "))

consecutiu = False
comptador = 0
quantsConsecutius = 0

while n != 0:
	anterior = n % 10
	aux = n
	aux = aux // 10
	seguent = aux % 10
	if anterior == seguent:
		consecutiu = True
		comptador = comptador + 1
	elif comptador >= 1:
		quantsConsecutius = quantsConsecutius + 1
		comptador = 0
	
	n = n // 10

if consecutiu == True:
	print "En el numero existeix com a minim " + str(quantsConsecutius) + " que son consecutius."
else:
	print "No hi ha cap numero consecutiu en el numero"
	
print
print "Gracies per la utilitzacio del meu programa"
print "Adeu!"