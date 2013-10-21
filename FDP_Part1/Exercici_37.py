print "Benvingut al meu programa"
print
n = int(raw_input("Escriu el nombre de termes que s'han de mostrar a la serie: "))
ts = 0

while 1 <= n:
	ts = (ts*2)+1
	n = n - 1
	print "Terme de la serie: " + str(ts)
	
print "Gracies per utilitzar el meu programa"
print "Adeu"