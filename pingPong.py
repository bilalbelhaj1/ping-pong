import turtle

window = turtle.Screen()
window.title("FIRST GAME BILAL ")
window.bgcolor("#1f651b")
window.setup(width=600, height=400)
window.tracer(0)

goal1 = turtle.Turtle()
goal1.speed(0)
goal1.shape("square")
goal1.color("black")
goal1.shapesize(stretch_wid=5, stretch_len=1)
goal1.penup()
goal1.goto(-290, 0)

goal2 = turtle.Turtle()
goal2.speed(0)
goal2.shape("square")
goal2.color("black")
goal2.shapesize(stretch_wid=5, stretch_len=1)
goal2.penup()
goal2.goto(290, 0)

circle = turtle.Turtle()
circle.shape("circle")
circle.shapesize(stretch_wid=2.5, stretch_len=2.5)
circle.speed(0)
circle.color("white")
circle.goto(0, 0)


lign1 = turtle.Turtle()
lign1.speed(0)
lign1.shape("square")
lign1.color("white")
lign1.penup()
lign1.shapesize(stretch_wid=20, stretch_len=0.2)

lign2 = turtle.Turtle()
lign2.speed(0)
lign2.shape("square")
lign2.penup()
lign2.color("white")
lign2.goto(0, 200)
lign2.shapesize(stretch_wid=0.2, stretch_len=30)

lign3 = turtle.Turtle()
lign3.speed(0)
lign3.shape("square")
lign3.color("white")
lign3.goto(0, -200)
lign3.penup()
lign3.shapesize(stretch_wid=0.2, stretch_len=30)

lign4 = turtle.Turtle()
lign4.speed(0)
lign4.shape("square")
lign4.penup()
lign4.color("white")
lign4.goto(300, 0)
lign4.shapesize(stretch_wid=20, stretch_len=0.2)

lign5 = turtle.Turtle()
lign5.speed(0)
lign5.shape("square")
lign5.penup()
lign5.color("white")
lign5.goto(-300, 0)
lign5.shapesize(stretch_wid=20, stretch_len=0.2)


player1 = turtle.Turtle()
player1.speed(0)
player1.color("#7886c9")
player1.shape("square")
player1.penup()
player1.shapesize(stretch_wid=3, stretch_len=1)
player1.goto(-240, 0)

player2 = turtle.Turtle()
player2.speed(0)
player2.color("#4986f8")
player2.shape("square")
player2.penup()
player2.shapesize(stretch_wid=3, stretch_len=1)
player2.goto(240, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=2, stretch_len=2)
ball.penup()
ball.color("#c7a67a")
ball.dx = 1
ball.dy = 1

score1 = 0
score2 = 0
score = turtle.Turtle()
score.penup()
score.hideturtle()
score.speed(0)
score.color("white")
score.goto(-150, 150)
score.write(f"Player1: {score1}    Player2: {score2}", font=("Courier", 16, "normal"))


def player1_up():
    y = player1.ycor()
    y += 40
    player1.sety(y)


def player1_down():
    y = player1.ycor()
    y -= 40
    player1.sety(y)


def player2_up():
    y = player2.ycor()
    y += 40
    player2.sety(y)


def player2_down():
    y = player2.ycor()
    y -= 40
    player2.sety(y)


def gameOver():
    window.bye()


window.listen()
window.onkeypress(player1_up, "w")
window.onkeypress(player1_down, "s")
window.onkeypress(player2_up, "Up")
window.onkeypress(player2_down, "Down")
window.onkeypress(gameOver, "e")



while True:

    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if player2.ycor() > 170:
        player2.sety(170)

    if player2.ycor() < -170:
        player2.sety(-170)

    if player1.ycor() > 170:
        player1.sety(170)

    if player1.ycor() < -170:
        player1.sety(-170)

    if ((ball.xcor() > 220) and (ball.xcor() < 240)) and (ball.ycor() > player2.ycor()-40) and (ball.ycor() < player2.ycor() + 40):
        ball.setx(220)
        ball.dx *= -1

    if ((ball.xcor() < -220) and (ball.xcor() > -240)) and (ball.ycor() > player1.ycor()-40) and (ball.ycor() < player1.ycor() + 40):
        ball.setx(-220)
        ball.dx *= -1

    if ball.ycor() > 180:
        ball.sety(180)
        ball.dy *= -1

    if ball.ycor() < -180:
        ball.sety(-180)
        ball.dy *= -1

    if (ball.xcor() > 280) and (ball.ycor() > 50 or ball.ycor() < -50):
        ball.setx(280)
        ball.dx *= -1

    if (ball.xcor() < -280) and (ball.ycor() < -50 or ball.ycor() > 50):
        ball.setx(-280)
        ball.dx *= -1

    if (ball.xcor() > 280) and (ball.ycor() < 50 or ball.ycor() > -50):
        ball.goto(0, 0)
        score1 += 1
        score.clear()
        score.write(f"Player1: {score1}    Player2: {score2}", font=("Courier", 16, "normal"))

    if (ball.xcor() < -280) and (ball.ycor() < 50 or ball.ycor() > -50):
        ball.goto(0, 0)
        score2 += 1
        score.clear()
        score.write(f"Player1: {score1}    Player2: {score2}", font=("Courier", 16, "normal"))