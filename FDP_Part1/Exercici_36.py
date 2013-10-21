print "Benvingut al meu programa"
print
dia = int(raw_input("Escriu el dia inicial: "))
mes = int(raw_input("Escriu el mes inicial: "))
dt = int(raw_input("Escriu els dies transcorreguts: "))

df = dia
mf = mes

while dt > 28:
	dt = dt - 28
	mf = mf + 1
		
df = df + dt

if df > 28:
	df = df - 28
	mf = mf + 1
		
print "Data resultat: " + str(df) + "/" + str(mf)
print "Gracies per utilitzar el meu programa"
print "Adeu!"