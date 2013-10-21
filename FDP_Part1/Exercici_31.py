print "Benvingut al meu programa"
print
num = int(raw_input("Escriu el numero del qual volem generar la taula de multiplicacio: "))

y = 0
for y in range(0,11):
	print str(num) + " x " + str(y) + " = " + str(num*y)