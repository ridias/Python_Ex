print "Benvingut al meu programa"
print

n = int(raw_input("Escriu la base de la potencia: "))
e = int(raw_input("Escriu la potencia: "))

resultat = 1

while e != 0:
	resultat = resultat * n
	e = e - 1

ultim = resultat % 10	

while resultat != 0:
	resultat = resultat // 10
	if resultat < 100:
		primer = resultat // 10
		resultat = 0
	
if ultim == primer:
	print "Existeix un numero on el primer numero i l'ultim son el mateix numero"
else:
	print "No existeix cap numero"
	
print
print "Gracies per utilitzar el meu programa"
print "Adeu!"