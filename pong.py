import turtle
import os
import winsound

wn = turtle.Screen()
wn.title("Pong by @Divyanshi")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


#A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation
ball.shape("square")
ball.color("white")

ball.penup()
ball.goto(0, 0)

ball.dx = 0.08
ball.dy = -0.08

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))



#Function

def paddle_a_up():
    y = paddle_a.ycor() #ycor is y coordinate from turtle module
    y += 20
    paddle_a.sety(y) #sety is set y coordinate from turtle module

def paddle_a_down():
    y = paddle_a.ycor() #ycor is y coordinate from turtle module
    y -= 20
    paddle_a.sety(y) #sety is set y coordinate from turtle module


def paddle_b_up():
    y_b = paddle_b.ycor() #ycor is y coordinate from turtle module
    y_b += 20
    paddle_b.sety(y_b) #sety is set y coordinate from turtle module

def paddle_b_down():
    y_b = paddle_b.ycor() #ycor is y coordinate from turtle module
    y_b -= 20
    paddle_b.sety(y_b) #sety is set y coordinate from turtle module


#Keyboard binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #when w is pressed, call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()


    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #os.system("afplay bounce.wav&") #for mac play sound
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) #for windows play sound
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 20, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 20, "normal"))


    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1