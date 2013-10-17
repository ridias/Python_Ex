print "Benvingut al meu programa"
print
no = raw_input("Nombre d'ous que desitja comprar: ")
tpo = raw_input("El tipus d'ous que desitja: ")

nd = int(no) // 12
ne = int(no) % 12

if tpo == "a":
	pd = 3
	pe = 0.3

if tpo == "b":
	pd = 2.5
	pe = 0.25

if tpo == "c":
	pd = 2
	pe = 0.2

	
total = (nd*pd) + (ne*pe)

print "Dotzenes: " + str(nd)
print "Escadussers: " + str(ne)
print "Import: " + str(total)
print
print "Gracies per utilitzar el meu programa"
print "Adeu"