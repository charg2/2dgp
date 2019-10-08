import turtle

for i in range(0,5) :
    for j in range(0,5) :
        turtle.penup();
        turtle.goto(i * 100, j * 100);
        turtle.pendown();
        turtle.forward(100);
        turtle.left(90);
        turtle.forward(100);
        turtle.left(90);
        turtle.forward(100);
        turtle.left(90);
        turtle.forward(100);
        turtle.left(90);

turtle.exitonclick();
