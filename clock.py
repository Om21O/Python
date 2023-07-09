import turtle as t
import time
s=t.Turtle()
t.bgcolor("brown")
s.speed(0)
s.shape("arrow")
x=0
y=0
s.home()
s.write((x,y))

y=-200
s.penup()
s.goto(x,y)
s.pendown()

s.begin_fill()
s.fillcolor("yellow")
s.circle(200)
s.end_fill()
s.penup()
s.home()
y=-140  
s.goto(x,y)
s.pendown()
s.begin_fill()
s.fillcolor("white")
s.circle(140)
s.end_fill()
s.penup() 
s.home()


s.left(90)

for i in range(12):
    s.right(360/12)
    s.forward(185)
    s.write((i+1))
    s.goto(0,0)
    

def draw_hour_arm():
    s.penup()
    s.home()
    s.right(180)
    s.pendown()
    s.pensize(7)
    s.forward(110)
    s.penup()
    s.home()
    
def draw_min_arm():
    s.penup()
    s.home()
    s.left(90)
    s.pendown()
    s.pensize(5)
    s.forward(140)
    s.penup()
    s.home()
draw_hour_arm()
draw_min_arm()


angle=0
while True:
    start=time.time()
    a=1
    if a == 1:
        s.penup()
        s.home()
        s.left(90)
        a=2
    s.right(angle)
    s.pendown()
    s.pensize(3)
    s.forward(130)
    time.sleep(1)
    s.undo()
    s.penup
    s.goto(0,0)
    angle+=360/60
        
t.done()