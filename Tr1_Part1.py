print "Benvingut al meu programa"
print
p1 = int(raw_input("Escriu el valor de p1: "))
p2 = int(raw_input("Escriu el valor de p2: "))
p3 = int(raw_input("Escriu el valor de p3: "))
p4 = int(raw_input("Escriu el valor de p4: "))

maxim = p1

if (p1 == 500) and (p2 == 500) and (p3 == 500) and (p4 == 500):
	print "Tots els llibres tenen un maxim de 500 pagines"
elif (p1 >= 500) and (p2 >= 500) and (p3 >= 500) and (p4 >=500):
	print "Hi ha un o mes d'un llibre que supera les 500 pagines."
	maxim = 500
	
if (p1 >= 500) or (p2 >= 500) or (p3 >= 500) or (p4 >= 500):
	print "Hi ha un o mes d'un llibre que supera les 500 pagines."

if (p1 >= maxim) and (p1 < 500):
	maxim = p1

if (p2 >= maxim) and (p2 < 500):
	maxim = p2
	
if (p3 >= maxim) and (p3 < 500):
	maxim = p3
	
if (p4 >= maxim) and (p4 < 500):
	maxim = p4
	
print "El maxim es: " + str(maxim)
print
print "Gracies per utilitza el meu programa"
print "Adeu"