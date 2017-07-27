import turtle as tt
import math


t = tt.Turtle()
ventana = tt.Screen()
tt.bgcolor("black")
t.color("blue")
t.pensize(3)
t.speed(1)

cantidad = 5
figura = 4
angulo = 360 / figura
largo = 50

for x in range(figura):

	t.forward(largo)
	
	if(x != (figura - 1)):
	
		t.right(angulo)

for x in range(cantidad - 1):

	largo = math.sqrt(largo**2 * 2) / 2
	print(largo)

	t.right(angulo / 2)
	t.forward(largo)
	largo *= 2

	for y in range(figura):
	
		t.right(angulo)
		t.forward(largo)

ventana.exitonclick()