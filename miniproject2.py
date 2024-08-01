#score
score1 = 0
score2 = 0
score = turtle.Turtle
score.speed(0)
score.color("white")
score.penup()
score.hideturtle
score.goto(0,0)
score.write("Playrr 1: 0 Player 2: 0", align="center", font=("Courier",24,"normal"))

#functions
def paddle1_up():
    y = paddle1.ycor() #set the y coordinate of the paddle1
    y += 20 #set the y coordinate of the paddle2
    paddle1.sety(y) #set the y of the paddle1 to the new y coordinate
def paddle1_down():
    y = paddle1.ycor() #set the y coordinate of the paddle1
    y -= 20 #set the y to decrease be20
    paddle1.sety(y) #set the y of the paddle1 to the new y coordinate

def paddle2_up():
    y = paddle2.ycor() #set the y coordinate of the paddle2
    y += 20 #set the y coordinate of the paddle2
    paddle2.sety(y) #set the y of the paddle2 to the new y coordinate
def paddle2_down():
    y = paddle2.ycor()  #set the y coordinate of the paddle2
    y -= 20 #set the y coordinate of the paddle2
    paddle2.sety(y) #set the y of the paddle2 to the new y coordinate

#keyboard blindings
w.listen() #tell the window to expect keyboard input
w.onkeypress(paddle1_up, "w") #when pressing w the function is invoked
w.onkeypress(paddle1_down, "s") #when pressing s the function is invoked
w.onkeypress(paddle2_up, "Up") #when pressing Up the function is invoked
w.onkeypress(paddle2_down, "Down") #when pressing Up the function is invoked

#ball
ball.dx = 2.5
ball.dy = 2.5

#main game loop
while True:
    w.update() #updates the the screen everytime the loop run

    #move the ball
    ball.setx(ball.xcor() + ball.dx) #ball starts at 0 and everytime loops run--->+2.5 xaxis
    ball.sety(ball.ycor() + ball.dy) #ball starts at 0 and everytime loops run--->+2.5 xaxis

    #border check , top border +300px , bottom border -300px ,ball is 20px
    if ball.ycor() > 290: #if ball is at top border
        ball.sety(290) #set y coordinate +290
        ball.dy *= -1 #reverse direction, making +2.5--->-2.5

    if ball.ycor() <- 290: #if ball is at bottom border
        ball.sety(-290) #set y coordinate +290
        ball.dy *= -1 #reverse direction, making +2.5--->-2.5

    if ball.xcor() > 390: #if ball is at right border
        ball.goto(0,0) #return ball to center
        ball.dx *= -1 #reverse the x direction
        score1 += 1
        score.clear()
        score.write("Playrr 1: {} Player 2: {}".format(score1,score2), align="center", font=("Courier",24,"normal"))

    if ball.xcor() <- 390: #if ball is at left border
        ball.goto(0,0) #return ball to center
        ball.dx *= -1 #reverse the x direction 
        score2 += 1
        score.clear()
        score.write("Playrr 1: {} Player 2: {}".format(score1,score2), align="center", font=("Courier",24,"normal"))
    #tasadom paddle and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.xcor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() > -340 and ball.xcor() < -350) and (ball.xcor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1