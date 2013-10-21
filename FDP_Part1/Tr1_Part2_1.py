print "Benvingut al meu programa"
print 
num = 10000
comptadorGuai = 0

while num <= 99999:
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
	num = num + 1

print "Nombre de numeros guais: " + str(comptadorGuai)