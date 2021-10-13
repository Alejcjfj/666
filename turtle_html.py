import turtle as t



def draw_square(side_lenght = 100, x = -100, y = -100, line_color = "red", fill_color = "brown"):
	#настройка
	t.pencolor(line_color)
	t.fillcolor(fill_color)
	t.penup()
	t.goto(x, y)
	t.pendown()

	#рисование
	t.begin_fill()
	t.forward(side_lenght)
	t.left(90)
	t.forward(side_lenght)
	t.left(90)
	t.forward(side_lenght)
	t.left(90)
	t.forward(side_lenght)
	t.left(90)
	t.end_fill()

	
	
	
#астройка
t.goto(0, 0)
t.shape("turtle")
t.speed(1)


# исование
draw_square(fill_color = "green")









t.done()
