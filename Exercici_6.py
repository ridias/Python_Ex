print "Benvingut al meu programa."
print
num = raw_input("Escriu un numero: ")
u = int(num) % 10
aux = int(num) // 10
d = aux % 10
c = aux //10
sum = u+d+c
print "La suma de les xifres es: " + str(sum)
print "Gracies per utilitzar el meu programa."
print "Adeu"