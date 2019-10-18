import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()



def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())



def draw_curve_4_points(p1, p2, p3, p4):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    point_list = [p1, p2, p3, p4];
    size = 4;
    for i in range(size):
        draw_curve(point_list[i], point_list[( i + 1 ) % size], point_list[( i + 2 ) % size]);


def draw_curve(begin, center, end):
    for i in range(0, 50, 2):
        t = i / 100;
        x = (2*t**2-3*t+1) * begin[0]+(-4*t**2+4*t) * center[0]+(2*t**2-t) * end[0];
        y = (2*t**2-3*t+1) * begin[1]+(-4*t**2+4*t) * center[1]+(2*t**2-t) * end[1];
        draw_point((x, y));
    draw_point(end);




prepare_turtle_canvas()

while True:
    draw_curve_4_points((-300, 200), (400, 350), (300, -300),(-200, -200));

turtle.done()