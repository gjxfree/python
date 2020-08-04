# 利用海龟画图 绘制一个奥运五环
import turtle

turtle.width(10)

turtle.color("blue")
turtle.circle(50)

turtle.penup()
turtle.goto(60,-50)
turtle.color("yellow")
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(120,0)
turtle.color("black")
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(180,-50)
turtle.color("green")
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(240,0)
turtle.color("red")
turtle.pendown()
turtle.circle(50)



