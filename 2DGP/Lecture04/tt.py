
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




def draw_curve_3_points(p1, p2, p3):
    draw_big_point(p1);
    draw_big_point(p2);
    draw_big_point(p3);

    for i in range(0 ,100, 2):
        t = i / 100;
        x = (2 * t**2 - 3 * t + 1) * p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0];
        y = (2 * t**2 - 3 * t + 1) * p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1];
        draw_point((x, y))

    draw_point(p3);


def draw_curve_4_points(p1, p2, p3, p4):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    points:list = [p1, p2, p3, p4];
    for i in range(3):
        draw_curve(points[i], points[(i+1)%4], points[(i+2)%4]);


    ## draw p1-p2
    #for i in range(0, 50, 2):
    #    t = i / 100
    #    x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
    #    y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
    #    draw_point((x, y))
    #draw_point(p2)

    ## draw p2-p3
    #for i in range(0, 50, 2):
    #    t = i / 100
    #    x = (2*t**2-3*t+1)*p2[0]+(-4*t**2+4*t)*p3[0]+(2*t**2-t)*p4[0]
    #    y = (2*t**2-3*t+1)*p2[1]+(-4*t**2+4*t)*p3[1]+(2*t**2-t)*p4[1]
    #    draw_point((x, y))
    #draw_point(p3)

    ## draw p3-p4
    #for i in range(0, 50, 2):
    #    t = i / 100
    #    x = (2*t**2-3*t+1)*p3[0]+(-4*t**2+4*t)*p4[0]+(2*t**2-t)*p1[0]
    #    y = (2*t**2-3*t+1)*p3[1]+(-4*t**2+4*t)*p4[1]+(2*t**2-t)*p1[1]
    #    draw_point((x, y))
    #draw_point(p4)

    # # draw p4-p1
    #for i in range(0, 50, 2):
    #    t = i / 100
    #    x = (2*t**2-3*t+1)*p4[0] +(-4*t**2+4*t)*p1[0] +(2*t**2-t)*p2[0]
    #    y = (2*t**2-3*t+1)*p4[1] +(-4*t**2+4*t)*p1[1] +(2*t**2-t)*p2[1]
    #    draw_point((x, y))
    #draw_point(p1)

def draw_curve(begin, center ,end):
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*begin[0]+(-4*t**2+4*t)*center[0]+(2*t**2-t)*end[0];
        y = (2*t**2-3*t+1)*begin[1]+(-4*t**2+4*t)*center[1]+(2*t**2-t)*end[1];
        draw_point((x, y))


prepare_turtle_canvas()

draw_curve_4_points((100, 200), (200, 300), (100,-100), (-200, 0));

turtle.done()