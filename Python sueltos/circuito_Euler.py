
import turtle as tt


class CircuitoEuler():

	def __init__(self, figura, cantidad, largo):
	
		self.tortuga = tt.Turtle()
		self.figura = figura
		self.cantidad = cantidad
		self.largo = largo
		self.ang = 360
		self.ventana = tt.Screen()
		tt.bgcolor("black")

		self.euler()

	def euler(self):
	
		self.definir()
		self.dibujar()
		self.circuito()
		self.ventana.exitonclick()

	def definir(self):
	
		self.ang /= self.figura

	def dibujar(self):
	
		self.tortuga.color("blue")
		self.tortuga.pensize(3)
		self.tortuga.speed(1)

		for x in range(self.figura):
		
			self.tortuga.right(self.ang)
			self.tortuga.forward(self.largo)

		for x in range(self.cantidad - 1):
		
			self.tortuga.right(self.ang / 2)
			self.tortuga.forward(self.largo)
			self.largo *= 2

			for x in range(self.figura):
			
				self.tortuga.right(self.ang)
				self.tortuga.forward(self.largo)

		self.tortuga.hideturtle()

	def circuito(self):
	
		self.tortuga.color("green")
		self.tortuga.right(self.ang)
		self.tortuga.showturtle()
		self.tortuga.speed(1)
		self.tortuga.dot(10)

		for x in range(self.cantidad):
		
			for y in range(2):
			
				self.tortuga.forward(self.largo)
				self.tortuga.right(self.ang)

			if(x != self.cantidad - 1):
			
				self.tortuga.forward(self.largo / 2)
				self.tortuga.right(self.ang)

				self.largo /= 2
				self.ang *= -1

		self.tortuga.forward(self.largo)
		self.ang *= -1

		if self.cantidad != 1:
		
			self.tortuga.right(self.ang)
			self.tortuga.forward(self.largo)

		for x in range(self.cantidad - 2):
		
			self.largo *= 2
			self.ang *= -1

			self.tortuga.right(self.ang)
			self.tortuga.forward(self.largo)


t = CircuitoEuler(3, 6, 20)