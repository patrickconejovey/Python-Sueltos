import turtle as tt


def octagono():

	ventana = tt.Screen()
	tt.bgcolor("black")
	t = tt.Turtle()
	t.pensize(3)
	t.color("green")
	t.hideturtle()
	t.speed(1)

	t.penup()

	t.right(270)
	t.forward(100)
	t.right(90)

	t.pendown()

	for x in range(8):
	
		t.right(45)
		t.forward(150)
		for y in range(4):
		
			t.right(90)
			t.forward(150)
	
	ventana.exitonclick()

octagono()