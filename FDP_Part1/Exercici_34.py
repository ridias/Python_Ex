print "Benvingut al meu programa"
print
dd = int(raw_input("Escriu el divident: "))
dr = int(raw_input("Escriu el divisor: "))

q = 0

while dd >= dr: 
	dd = dd - dr
	q = q + 1
	

print "El quocient enter es: " + str(q)
print "El residu es: " + str(dd)
print "Gracies per utilitzar el meu programa"
print "Adeu"