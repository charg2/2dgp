import turtle;

def forward_left():
    turtle.stamp();
    turtle.setheading(180);
    turtle.forward(50);
    turtle.stamp();

def forward_right():
    turtle.stamp();
    turtle.setheading(0);
    turtle.forward(50);
    turtle.stamp();

def forward_up():
    turtle.stamp();
    turtle.setheading(90);
    turtle.forward(50);
    turtle.stamp();

def forward_down():
    turtle.stamp();
    turtle.setheading(270);
    turtle.forward(50);
    turtle.stamp();

def restart():
    turtle.reset();

turtle.shape("turtle");

turtle.onkey(forward_up, 'w');
turtle.onkey(forward_left, 'a');
turtle.onkey(forward_down, 's');
turtle.onkey(forward_right, 'd');
turtle.onkey(restart, 'Escape');

turtle.listen();
turtle.exitonclick();
