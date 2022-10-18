import turtle
import os

window = turtle.Screen()
window.title("Pong by Josh")
window.bgcolor("black")
window.setup(width = 800,  height = 600)
window.tracer(0)

score_a = 0
score_b = 0

#hits = 0
xspeed = 1
yspeed = 1

#paddle left
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle right
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#key binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "i")
window.onkeypress(paddle_b_down, "k")

while True:
    window.update()
    
    #keeps paddles on screen
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
        
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)
    
    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 290:
        ball.sety(290)
        #hits += 1
        #if hits%6 == 0:
         #   yspeed = yspeed + .25
         #   xspeed = xspeed + .25
         #   hits = 1
            
        ball.dy *= -yspeed
        os.system("afplay pong.wav&")
    
    if ball.ycor() < -290:
        ball.sety(-290)
        #hits += 1
        #if hits%6 == 0:
        #    yspeed = yspeed + .25
        #    xspeed = xspeed + .25
        #    hits = 1
            
        ball.dy *= -yspeed
        os.system("afplay pong.wav&")
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        xspeed = 1
        yspeed = 1
        ball.dx = -xspeed
        #ball.dy = -yspeed
        #hits = 1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        xspeed = 1
        yspeed = 1
        ball.dx = -xspeed
        #ball.dy = -yspeed
        #hits = 1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

        
    if ((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40)):
        ball.setx(340)
        #hits += 1
        #if hits%6 == 0:
          #  yspeed = yspeed + .25
           # xspeed = xspeed + .25
            #hits = 1
            
        ball.dx *= -xspeed
        os.system("afplay pong.wav&")
        
    if ((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40)):
        ball.setx(-340)
        #hits += 1
        
       # if hits%6 == 0:
       #    yspeed = yspeed + .25
        #   xspeed = xspeed + .25
          #  hits = 1
        ###
            
        ball.dx *= -xspeed
        os.system("afplay pong.wav&")
        
