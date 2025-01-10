#Luisa Gorman and Alexis Golland
#Period 3 9/10/24
#Line Project

#Initialize
import turtle
luisa = turtle.Turtle()
alexis = turtle.Turtle()

#Functions
#helps turn arrow around when needed
#Coded:Luisa and Alexis
def turnAround():
    luisa.left(180)
#draws all 3 legs on both sides
#Coded: Luisa left and Alexis right
def crabLegsLeft():
    for i in range(3):
        luisa.color("red")
        luisa.pensize(20)
        luisa.circle(60,120)
        turnAround()
        luisa.circle(-60,120)
        luisa.left(90)
        luisa.forward(50)
        luisa.left(75)
def crabLegsRight():
    for i in range(3):
        alexis.color("red")
        alexis.pensize(20)
        alexis.circle(-60,120)
        alexis.left(180)
        alexis.circle(60,120)
        alexis.right(90)
        alexis.forward(50)
        alexis.right(75)
#draws entire crab image
#Coded:Collaboration between Luisa and Alexis
def drawCrab():
    #Head-Luisa&Alexis
    #drew head
    luisa.speed(8)
    luisa.penup()
    luisa.goto(0,-100)
    luisa.pendown()
    luisa.begin_fill()
    luisa.color("red")    
    luisa.circle(150,360)
    luisa.end_fill()
    luisa.penup()
    #Eyes-Luisa&Alexis
    #drew eyes and pupils
    luisa.left(90)
    luisa.forward(150)
    luisa.left(90)
    luisa.forward(75)
    luisa.pendown()
    luisa.dot(70,"white")
    luisa.dot(45,"black")
    luisa.penup()
    turnAround()
    luisa.forward(150)
    luisa.pendown()
    luisa.dot(70,"white")
    luisa.dot(45,"black")
    luisa.penup()
    #Mouth-Luisa&Alexis
    #drew the crabs smirk
    luisa.right(90)
    luisa.forward(70)
    luisa.pendown()
    luisa.pensize(10)
    luisa.color("black")
    luisa.circle(-50,120)
    luisa.penup()
    #LegsLeft-Luisa
    #drew the three left legs
    luisa.left(30)
    luisa.forward(90)
    luisa.pendown()
    luisa.left(30)
    crabLegsLeft()
    luisa.penup()
    #HandsLeft-Luisa
    #drew the left claw
    luisa.right(75)
    luisa.forward(30)
    luisa.left(80)
    luisa.pensize(50)
    luisa.pendown()
    luisa.forward(65)
    luisa.right(50)
    luisa.forward(65)
    luisa.pensize(25)
    luisa.left(55)
    luisa.begin_fill()
    luisa.color("red")
    luisa.circle(-70,120)
    luisa.right(125)
    luisa.forward(120)
    luisa.end_fill()
    turnAround()
    luisa.begin_fill()
    luisa.pensize(15)
    luisa.right(75)
    luisa.circle(80,70)
    luisa.left(125)
    luisa.forward(70)
    luisa.end_fill()
    #LegsRight-Alexis
    #drew the three right legs
    alexis.speed(8)
    alexis.penup
    alexis.right(90)
    alexis.forward(70)
    alexis.right(120)
    alexis.right(150)
    alexis.forward(90)
    alexis.pendown()
    alexis.right(30)
    crabLegsRight()
    #ClawsRight-Alexis
    #drew the right claw
    alexis.left(75)
    alexis.forward(30)
    alexis.right(80)
    alexis.pensize(50)
    alexis.forward(65)
    alexis.left(50)
    alexis.forward(65)
    alexis.pensize(25)
    alexis.right(55)
    alexis.begin_fill()
    alexis.color("red")
    alexis.circle(70,120)
    alexis.left(125)
    alexis.forward(120)
    alexis.end_fill()
    alexis.left(180)
    alexis.pensize(15)
    alexis.left(75)
    alexis.begin_fill()
    alexis.circle(-80,70)
    alexis.right(125)
    alexis.forward(70)
    alexis.end_fill()

#main
drawCrab()



