import math
from math import *

print "Benvingut al meu programa."
print
a = int(raw_input("Primer valor: "))
b = int(raw_input("Segon valor: "))
c = int(raw_input("Tercer valor: "))

if a == 0:
	print "No es tracta d'una sequencia de segon grau."
else:
	dscr = (b*b) - (4*a*c)
	if dscr < 0:
		print "No te solucio real"
	else:
		x1 = (-b + math.sqrt(dscr))/(2*a)
		x2 = (-b - math.sqrt(dscr))/(2*a)
		print "Primera solucio" + str(x1)
		print "Segona solucio" + str(x2)
		
print "Gracies per utilitzar el meu programa"
print "Adeu"