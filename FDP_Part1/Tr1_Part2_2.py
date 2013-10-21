print "Benvingut al meu programa"
print 
num = 10000
comptadorGuai = 0

for num in range(10000, 100000):
	aux = num
	u = aux % 10
	aux = aux // 10
	d = aux % 10
	aux = aux // 10
	c = aux % 10
	aux = aux // 10
	mu = aux % 10
	aux = aux // 10
	md = aux % 10
	if (u % 2 == 1) and (c % 2 == 1) and (md % 2 == 1) and (d % 2 == 0) and (mu % 2 == 0):
		comptadorGuai = comptadorGuai + 1

print "Nombre de numeros guais: " + str(comptadorGuai)
print 
print "Gracies per utilitzar el meu programa"
print "Adeu"