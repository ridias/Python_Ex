import time
import os

print "Bienvenido a mi programa"
print "Este programa consistira en un control de horario"
print "Dispondremos de la informacion basica de los empleados y cuando pueden estar en un lugar y en otro"



def guardarEnLista(elemento, *algomas):
	lista = []
	lista.append(elemento)
	
	for cosa in algomas:
		lista.append(cosa)
	
	return lista

				
def relojActual(cambiar):
	if cambiar == 59:
		cambiar = 0
	elif cambiar == 10:
		os.system('cls')				#equivalente a clrscr() de pascal o c++ importando arriba
		
	
	return cambiar

			
def relojEmpresarial(horActual, minutosActual, segundosActual, limite, lugar):

	comptadorSegundos = 0
	comptadorMinutos = 0
	comptadorHoras = 0
	while limite != 0:
		if comptadorSegundos != 60:
			time.sleep(1)
			segundosActual = segundosActual + 1
			segundosActual = relojActual(segundosActual)
			comptadorSegundos = comptadorSegundos + 1
			print "Hora actual: ", horActual, ":", minutosActual, ":", segundosActual
			print "Tiempo que te queda: ", comptadorHoras, ":", comptadorMinutos, ":", comptadorSegundos
			if comptadorSegundos == 59:
				comptadorSegundos = 0
				comptadorMinutos = comptadorMinutos + 1
				minutosActual = minutosActual + 1
				minutosActual = relojActual(minutosActual)
				if comptadorMinutos == 59:
					comptadorMinutos = 0
					comptadorHoras = comptadorHoras + 1
					horActual = horActual + 1
					limite = limite - 1
					
	if limite == 0 and lugar == "Gym":
		print "Ya has terminado tu hora de ejercicio en el gymnasio"
	elif limite == 0 and lugar == "Trabajo":
		print "Ya has acabado de trabajar, te puedes ir a casa"
	
	
	
class Empleado(object):
	
	#atributos principales
	def __init__(self, id, nombre, apellido, edad, oficio, departamento, sala, limite, entrada, salida):
		self.id = id
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.oficio = oficio
		self.departamento = departamento
		self.sala = sala
		self.limite = limite
		self.entrada = entrada
		self.salida = salida
		permitirAcceso = False
		lista = guardarEnLista(id, nombre, apellido, edad, oficio, departamento, sala, limite, permitirAcceso)
		
	
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
		elif elemento == "sala" or elemento == "sala":
			return self.sala
			print "Has recibido perfectamente la informacion"
		elif elemento == "limite" or elemento == "Limite":
			return self.limite
			print "Has recibido perfectamente la informacion"
		elif elemento == "entrada" or elemento == "Entrada":
			return self.entrada
			print "Has recibido perfectamente la informacion"
		elif elemento == "salida" or elemento == "Salida":
			return self.salida
			print "Has recibido perfectamente la informacion"
			
	#funcion para obtener toda la informacion de empleado en una lista		
	def getTodoEmpleado(self):
		print lista
	
	
	#Funcion de modificar la totalidad de la informacion de un Empleado
	def setTodoEmpleado(self, id, nombre, apellido, edad, oficio, departamento, sala, limite, entrada, salida):
		self.id = id
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.oficio = oficio
		self.departamento = departamento
		self.sala = sala
		self.limite = limite
		self.entrada = entrada
		self.salida = salida
		permitirAcceso = False
		
		informacion = guardarEnLista(id, nombre, apellido, edad, oficio, departamento, sala, limite, entrada, salida, permitirAcceso)
		print "La informacion se ha cambiado perfectamente"
		print informacion
		
	
	#funcion que permite modificar un atributo del objeto
	def setEmpleado(self, elemento):
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
		elif elemento == "sala" or elemento == "Sala":
			self.sala = sala
			lista.insert(6, elemento)
			print "La informacion se ha cambiado perfectamente"
		elif elemento == "limite" or elemento == "Limite":
			self.limite = limite
			lista.insert(7,elemento)
			print "La informacion se ha cambiado perfectamente"
		elif elemento == "entrada" or elemento == "Entrada":
			self.entrada = entrada
			lista.insert(8,elemento)
			print "La informacion se ha cambiado perfectamente"
		elif elemento == "salida" or elemento == "Salida":
			self.salida = salida
			lista.insert(9,elemento)
			print "La informacion se ha cambiado perfectamente"
	
	
	#funcion que presenta la informacion del objeto creado
	def datosEmpleado(self):
		print "Ficha de empleado:"
		print "Identificacion: ", self.id
		print "Nombre: ", self.nombre
		print "Apellidos: ", self.apellido
		print "Edad: ", self.edad
		print "Oficio: ", self.oficio
		print "Departamento: ", self.departamento
		print "Sala en la que esta ahora: ", self.sala
		print "Limite de gimnasio: ", self.limite
		print "Hora de entrada del trabajo: ", self.entrada
		print "Hora de salida del trabajo: ", self.salida
		
		
	#funcion que permite verificar si un empleado esta en el gym o en el trabajo, fuera de hora	
	def verificar(lista):
	comptador = 0
	for elemento in lista:
		if elemento == False or (elemento == "Gym" or elemento == "gym"):
			comptador = comptador + 1
			if comptador == 2:
				print "No puedes estar en el gym, has depasado la hora"
			else:
				print "Puedes acceder a la sala Gym, tienes 1 hora para hacer ejercicio a partir de ahora"
		

#Pruebas	
Carlos = Empleado(1, "Carlos", "Dias", 45, "Programador", "Java", "Gym", 1, 8, 16)
Ellie = Empleado(1, "Carlos", "Dias", 45, "Programador", "Java", "Gym", 1, 8, 16)
#carlos.setTodoEmpleado(2, "Carlos", "Dias", 42, "Programador", "Java")

listaEmpleados = []
listaEmpleados.append(Carlos)
listaEmpleados.append(Ellie)

print listaEmpleados[1].datosEmpleado()

#relojEmpresarial(18,9,0,1,"Gym")
		