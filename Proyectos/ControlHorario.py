print "Bienvenido a mi programa"
print "Este programa consistira en un control de horario"
print "Dispondremos de la informacion basica de los empleados y cuando pueden estar en un lugar y en otro"


def guardarEnLista(elemento, *algomas):
	lista = []
	lista.append(elemento)
	
	for cosa in algomas:
		lista.append(cosa)
	
	return lista
	
	

class Empleado(object):
	
	#atributos principales
	def __init__(self, id, nombre, apellido, edad, oficio, departamento):
		self.id = id
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.oficio = oficio
		self.departamento = departamento
		lista = guardarEnLista(id, nombre, apellido, edad, oficio, departamento)
		
	
	#obtener una informacion especifica del empleado
	def getEmpleado(self):
		print "La unica informacion a la que puedes acceder son (escoge entre uno de estos): id, nombre, apellido, edad, oficio, departamento."
		elemento = str(raw_input("Que informacion quieres saber sobre algun empleado: "))
		
		if elemento == "id" or elemento == "Id":
			return self.id
			print "Has recibido perfectamente la informacion"
		elif elemento == "nombre" or elemento == "Nombre":
			return self.nombre
			print "Has recibido perfectamente la informacion"
		elif elemento == "apellido" or elemento == "Apellido":
			return self.apellido
			print "Has recibido perfectamente la informacion"
		elif elemento == "edad" or elemento == "Edad":
			return self.edad
			print "Has recibido perfectamente la informacion"
		elif elemento == "oficio" or elemento == "Oficio":
			return self.oficio
			print "Has recibido perfectamente la informacion"
		elif elemento == "departamento" or elemento == "Departamento":
			return self.departamento
			print "Has recibido perfectamente la informacion"
			
	def getTodoEmpleado(self):
		print lista
	
	
	#Funcion de modificar la totalidad de la informacion de un Empleado
	def setTodoEmpleado(self, id, nombre, apellido, edad, oficio, departamento):
		self.id = id
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.oficio = oficio
		self.departamento = departamento
		
		informacion = guardarEnLista(id, nombre, apellido, edad, oficio, departamento)
		print "La informacion se ha cambiado perfectamente"
		print informacion
		
	def setEmpleado(self, elemento)
		print "La unica informacion que puedes cambiar son (escoge entre uno de estos): id, nombre, apellido, edad, oficio, departamento."
		elemento = str(raw_input("Que informacion quieres cambiar sobre algun empleado: "))
		
		if elemento == "id" or elemento == "Id":
			self.id = elemento
			lista.insert(0, elemento)
			print "La informacion se ha cambiado perfectamente"
		elif elemento == "nombre" or elemento == "Nombre":
			self.nombre = elemento
			lista.insert(1, elemento)
			print "La informacion se ha cambiado perfectamente"
		elif elemento == "apellido" or elemento == "Apellido":
			self.apellido = elemento
			lista.insert(2, elemento)
			print "La informacion se ha cambiado perfectamente"
		elif elemento == "edad" or elemento == "Edad":
			self.edad = elemento
			lista.insert(3, elemento)
			print "La informacion se ha cambiado perfectamente"
		elif elemento == "oficio" or elemento == "Oficio":
			self.oficio = elemento
			lista.insert(4, elemento)
			print "La informacion se ha cambiado perfectamente"
		elif elemento == "departamento" or elemento == "Departamento":
			self.departamento = elemento
			lista.insert(5, elemento)
			print "La informacion se ha cambiado perfectamente"
			
			
		
	

#Pruebas	
carlos = Empleado(1, "Carlos", "Dias", 45, "Programador", "Java")
carlos.setTodoEmpleado(2, "Carlos", "Dias", 42, "Programador", "Java")

		
		