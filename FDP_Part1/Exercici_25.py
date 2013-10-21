print "Benvingut al meu programa"
print
dn = int(raw_input("Escriu el teu dia de naixement: "))
mn = int(raw_input("Escriu el teu mes de naixement: "))
an = int(raw_input("Escriu el teu any de naixement: "))
da = int(raw_input("Escriu el dia actual: "))
ma = int(raw_input("Escriu el mes actual: "))
aa = int(raw_input("Escriu el any actual: "))

edat = aa - an
if ma < mn:
	edat = edat - 1
elif ma == mn:
	if da < dn:
		edat = edat - 1
		
print "Tens " + str(edat) + " anys."
print "Gracies per utilitzar el meu programa"
print "Adeu"