import turtle as t
w=t.Screen()
w.title(" Our pong game")
w.bgcolor("pink")
w.setup(width=780,height=580)
w.tracer(0)  #turn  automatic screen updates on or off

#create first player "left paddele"
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_len=1,stretch_wid=5)
leftpaddle.penup()
leftpaddle.goto(x=350,y=0)

#create second player "right paddele"
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_len=1,stretch_wid=5)
rightpaddle.penup()
rightpaddle.goto(x=-350,y=0)


#creating a ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup() 
ball.goto(x=5,y=5)
#score
score1 = 0
score2 = 0
score=t.Turtle()
score.speed(0)
score.penup()
# score.hideturtle()
score.goto(x=0,y=260)
score.write( "player1=0,player2=0",align="center" ,)

#functions
def paddle1_up():
    y = rightpaddle.ycor() #set the y coordinate of the paddle1
    y += 90 #set the y coordinate of the paddle2
    rightpaddle.sety(y) #set the y of the paddle1 to the new y coordinate
def paddle1_down():
    y = rightpaddle.ycor() #set the y coordinate of the paddle1
    y -= 90 #set the y to decrease be20
    rightpaddle.sety(y) #set the y of the paddle1 to the new y coordinate

def paddle2_up():
    y = leftpaddle.ycor() #set the y coordinate of the paddle2
    y += 90 #set the y coordinate of the paddle2
    leftpaddle.sety(y) #set the y of the paddle2 to the new y coordinate
def paddle2_down():
    y = leftpaddle.ycor()  #set the y coordinate of the paddle2
    y -= 90 #set the y coordinate of the paddle2
    leftpaddle.sety(y) #set the y of the paddle2 to the new y coordinate

#keyboard blindings
w.listen() #tell the window to expect keyboard input
w.onkeypress(paddle1_up, "w") #when pressing w the function is invoked
w.onkeypress(paddle1_down, "s") #when pressing s the function is invoked
w.onkeypress(paddle2_up, "Up") #when pressing Up the function is invoked
w.onkeypress(paddle2_down, "Down") #when pressing Up the function is invoked

#ball
ball.dx = 0.5
ball.dy = 0.5

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

    if ball.xcor() > 350: #if ball is at right border
        ball.goto(0,0) #return ball to center
        ball.dx *= -1 #reverse the x direction
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1,score2), align="center", font=("Courier",15,"normal"))

    if ball.xcor() <- 350: #if ball is at left border
        ball.goto(0,0) #return ball to center
        ball.dx *= -1 #reverse the x direction 
        score2 += 1
        score.clear()
        score.write("Playrr 1: {} Player 2: {}".format(score1,score2), align="center", font=("Courier",15,"normal"))
    #tasadom paddle and ball
    if (ball.xcor() > 350 and ball.xcor() < 350) and (ball.ycor() < leftpaddle.ycor() + 50 and ball.ycor() > leftpaddle.ycor() - 50):
        ball.setx(350)
        ball.dx *= -1

    if (ball.ycor() > -350 and ball.ycor() < -350) and (ball.ycor() < rightpaddle.ycor() + 50 and ball.ycor() > rightpaddle.ycor() - 50):
        ball.setx(-350)
        ball.dy *= -1
        