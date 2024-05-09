import turtle as t 
import random as r

#create a turtle
t.colormode(255)
squirtle= t.Turtle()
squirtle.shape("circle")
squirtle.speed(0)

wn = t.Screen()
wn.bgcolor('sky blue')
wn.addshape('santa.gif')

def tree():     #makes tree and star
    squirtle.begin_fill()
    squirtle.color('green')
    squirtle.lt(60)
    squirtle.fd(100)
    squirtle.rt(120)
    squirtle.fd(100)
    squirtle.rt(120)
    squirtle.fd(100)
    squirtle.teleport(0,35)
    squirtle.rt(120)
    squirtle.fd(100)
    squirtle.rt(120)
    squirtle.fd(100)
    squirtle.rt(120)
    squirtle.fd(100)
    squirtle.teleport(0,70)
    squirtle.rt(120)
    squirtle.fd(100)
    squirtle.rt(120)
    squirtle.fd(100)
    squirtle.rt(120)
    squirtle.fd(100)
    squirtle.end_fill()
    squirtle.rt(180)
    squirtle.teleport(25,0)
    squirtle.color(150,100,0)
    squirtle.begin_fill()
    for i in range(2):
        squirtle.fd(50)
        squirtle.rt(90)
        squirtle.fd(25)
        squirtle.rt(90)
    squirtle.end_fill()
    squirtle.teleport(37,165)   #starts star
    squirtle.begin_fill()
    squirtle.color(255,255,0)
    for i in range(5):
        squirtle.fd(10)
        squirtle.rt(-72)
        squirtle.fd(10)
        squirtle.rt(72+72)
    squirtle.end_fill()
def ornaments():    #makes the ornaments
    squirtle.shape('circle')
    squirtle.turtlesize(.6)
    squirtle.teleport(15,40)
    squirtle.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))
    squirtle.stamp()
    squirtle.teleport(50,70)
    squirtle.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))
    squirtle.stamp()
    squirtle.teleport(75,90)
    squirtle.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))
    squirtle.stamp()
    squirtle.teleport(25,64)
    squirtle.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))
    squirtle.stamp()
    squirtle.teleport(17,6)
    squirtle.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))
    squirtle.stamp()
    squirtle.teleport(60,22)
    squirtle.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))
    squirtle.stamp()
    squirtle.teleport(31,100)
    squirtle.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))
    squirtle.stamp()
def present():  #makes the present
    squirtle.teleport(-20,-10)
    squirtle.color("yellow")
    squirtle.begin_fill()
    squirtle.heading()
    for i in range(4):
        squirtle.fd(50)
        squirtle.rt(90)
    squirtle.end_fill()
    squirtle.teleport(0,-10)
    squirtle.color("red")
    squirtle.begin_fill()
    for i in range(2):
        squirtle.fd(10)
        squirtle.rt(90)
        squirtle.fd(50)
        squirtle.rt(90)
    squirtle.end_fill()
def snowman():  #makes snowman
    squirtle.teleport(-60,-10)
    squirtle.color("white")
    squirtle.turtlesize(3)
    squirtle.stamp()
    squirtle.teleport(-60,35)
    squirtle.turtlesize(2)
    squirtle.stamp()
    squirtle.teleport(-60,64)
    squirtle.turtlesize(1)
    squirtle.stamp()
def sun():  #makes the sun
    squirtle.teleport(110,150)
    squirtle.color("yellow")
    squirtle.begin_fill()
    for i in range(360):
        squirtle.fd(1)
        squirtle.lt(1)
    squirtle.end_fill()
def hill(): # makes the ground
    squirtle.color("white")
    squirtle.teleport(0,-300)
    squirtle.turtlesize(30)
    squirtle.stamp()
    squirtle.turtlesize(1)
    squirtle.teleport(0,0)
def cookies():  #makes cookies
    squirtle.color(200,150,0)
    squirtle.teleport(77,-25)
    squirtle.stamp()
    squirtle.teleport(90,-20)
    squirtle.stamp()
    squirtle.teleport(81,-30)
    squirtle.stamp()


hill()
tree()
ornaments()
present()
snowman()
sun()
cookies()
squirtle.teleport(-200,200)
squirtle.write("Merry Christmas")
squirtle.teleport(-75,-100)
squirtle.shape('santa.gif')


snowflakes=[]
#creat a bunch of turltles
for i in range(75):
    turtle =t.Turtle(shape='circle')
    turtle.color('white')
    turtle.turtlesize(.3)
    snowflakes.append(turtle)
#iterate through the list of turtles
for s in snowflakes:
    s.teleport(r.randint(-300,300),r.randint(300,900))
while True:
    #move each turtle
    for s in snowflakes:
        newX = s.xcor()-r.randint(-10,10)
        newY = s.ycor()-9
        s.teleport(newX,newY)
    #reset the snow to the sky
        if s.ycor() < -300:
            s.stamp()
            s.teleport(r.randint(-300,300),r.randint(300,900))



wn.mainloop() 