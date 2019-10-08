import turtle;

def draw_circle(x, y, r):
    turtle.penup();
    turtle.goto(x, y);
    turtle.stamp();
    turtle.setheading(0);
    turtle.forward(r);
    turtle.pendown();
    turtle.setheading(90);
    turtle.circle(r);

turtle.shape("turtle");

for x,y,r in [ (0, 0, 50) , (200, 200, 100), (100, -100, 50)]:
    draw_circle (x, y, r);

turtle.exitonclick();
