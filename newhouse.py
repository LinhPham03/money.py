cao = int (input ('Nhập chiều cao ngôi nhà: '))
mai = int (input ('Nhập độ dài cạnh mái: '))
cao_ongkhoi= int (input ('Nhập chiều cao ống khói: '))
rong_ongkhoi= int (input ('Nhập độ rộng ống khói: '))
tan = int(input('Nhập số đo cạnh tán cây: '))
goc = int(input('Nhập số đo góc của thân cây: '))

import math
cao_cay= tan/(4*math.cos(goc))
cao_cua = 3/4*cao
dai = mai+50

import turtle
turtle.setup(1000, 1000)

turtle.penup()
turtle.goto(0,300)
turtle.pendown()

for i in range (3):
    turtle.forward(mai)
    turtle.left(120)

for i in range (2):
    turtle.forward (dai)
    turtle.right(90)
    turtle.forward(cao)
    turtle.right(90)

turtle.left(60)
turtle.forward(mai)
turtle.right(120)
turtle.forward(mai/2)

turtle.left(150)
turtle.forward(cao_ongkhoi)
turtle.right(90)
turtle.forward(rong_ongkhoi)
turtle.right(90)
turtle.forward(cao_ongkhoi+cao-rong_ongkhoi)

turtle.penup()
turtle.goto(0,300)
turtle.pendown()

turtle.forward (cao)
turtle.left(90)
turtle.forward(dai/4)

for i in range (2):
    turtle.forward(dai/2)
    turtle.left(90)
    turtle.forward(cao_cua)
    turtle.left(90)

turtle.penup()
turtle.goto(-100,250)
turtle.pendown()

for i in range (3):
    turtle.right(120)
    turtle.forward(tan)
    turtle.left(120)
    turtle.forward(tan)
    turtle.left(120)
    turtle.forward(tan)

    turtle.left(120)
    turtle.forward(tan)
    turtle.left(120)
    turtle.forward(tan/2)

#thân cây
turtle.backward(tan/8)
turtle.right(180-goc)
turtle.forward(cao_cay)
turtle.left(180-goc)
turtle.forward(6/8*tan)
turtle.left(180-goc)
turtle.forward(cao_cay)

turtle.penup()
turtle.goto(300,250)
turtle.pendown()
turtle.left(180+goc)

for i in range (3):
    turtle.right(120)
    turtle.forward(tan)
    turtle.left(120)
    turtle.forward(tan)
    turtle.left(120)
    turtle.forward(tan)

    turtle.left(120)
    turtle.forward(tan)
    turtle.left(120)
    turtle.forward(tan/2)

#thân cây
turtle.backward(tan/8)
turtle.right(180-goc)
turtle.forward(cao_cay)
turtle.left(180-goc)
turtle.forward(6/8*tan)
turtle.left(180-goc)
turtle.forward(cao_cay)

turtle.done()