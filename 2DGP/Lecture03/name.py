import turtle



turtle.forward(10);


turtle.penup();
turtle.goto(0, -10);
turtle.pendown();

turtle.forward(10);
turtle.right(120);
turtle.forward(17);
turtle.forward(-7);
turtle.left(90);
turtle.forward(10);

# ㅏ 위치로 
turtle.penup();
turtle.goto(20, 0);
turtle.pendown();

turtle.left(30);
turtle.right(90);

turtle.forward(30);
turtle.forward(-15);
turtle.left(90);

turtle.forward(10);

# ㅈ 위치로
turtle.penup();
turtle.goto(40, -10);
turtle.pendown();

# ㅈ
turtle.forward(10);
turtle.right(120);
turtle.forward(17);
turtle.forward(-7);
turtle.left(90);
turtle.forward(10);

# ㅣ#
turtle.penup();
turtle.goto(65, 0);
turtle.pendown();

# ㅣ 그리기
turtle.left(30);
turtle.right(90);
turtle.forward(30);

# 환 이동 
turtle.penup();
turtle.goto(90, 0);
turtle.pendown();
turtle.left(90);
turtle.forward(10);

## 환 이동 
turtle.penup();
turtle.goto(90, -10);
turtle.pendown();


turtle.forward(15);

turtle.penup();
turtle.goto(95, -25);
turtle.pendown();

turtle.circle(8);

turtle.right(90);
turtle.forward(5);

turtle.right(90);
turtle.forward(-5);
turtle.forward(15);

turtle.forward(-5);
turtle.left(90);
turtle.forward(5);
turtle.left(90);
turtle.forward(10);


#ㅏ
turtle.penup();
turtle.goto(110, 0);
turtle.pendown();


turtle.right(90);

turtle.forward(30);
turtle.forward(-15);
turtle.left(90);
turtle.forward(15);

turtle.exitonclick();
