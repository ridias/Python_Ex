print "Benvingut al meu programa"
print
a = int(raw_input("Escriu el nombre de litres que entraran per minut: "))
b = int(raw_input("Escriu el nombre de litres que sortiran per minut: "))
l = int(raw_input("Escriu el volum inicial de la banyera: "))

while (l <= 250) and (l > 0):
	l = l + a - b
	print "Minut: " + str(x) + "; Litres: " + str(l)
	x = x + 1
	

if l > 250:
	print "Sobreixis al cap de: " + str(x) + " minuts"
else: 
	print "Buida al cap de: " + str(x) + " minuts"
	
print "Gracies per utilitzar el meu programa"
print "Adeu"
	