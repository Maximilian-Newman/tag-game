import turtle
import time

speed = 5

screen = turtle.Screen()

turtle.penup()
turtle.speed(0)
turtle.hideturtle()
turtle.goto(0, 200)
turtle.write("Tag", align="center", font=("arial", 30, "bold"))
turtle.goto(0, 180)
turtle.write("You are blue", align="center", font=("arial", 15, "bold"))
turtle.goto(0, 160)
turtle.write("use arrows to turn", align="center", font=("arial", 15, "bold"))

player = turtle.Turtle()
player.penup()
player.speed(0)
player.goto(100, 0)
player.color("blue")

tager = turtle.Turtle()
tager.penup()
tager.speed(0)
tager.goto(-100, 0)
tager.color("red")

def right():
    player.right(speed * 2)
def left():
    player.left(speed * 2)

screen.listen()
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")

time.sleep(2)

playing = True
last_tager_update = 0

while playing:
    turtle.forward(0)
    
    player.forward(speed)
    tager.forward(speed)

    if last_tager_update < time.time() - 0.5:
        tager.forward(1)# to make the tager just a tiny bit faster than the player
        
        n_head = tager.towards(player)
        c_head = tager.heading()
        a = n_head - c_head
        a = (a + 180) % 360 - 180

        if a > speed * 2:
            tager.left(speed * 1.9)
        elif a < -speed * 2:
            tager.right(speed * 1.9)
        else:
            tager.left(a)
            last_tager_update = time.time()

    if player.pos()[0] > 290:
        player.setheading(180)
    if player.pos()[0] < -290:
        player.setheading(0)
    if player.pos()[1] > 280:
        player.setheading(270)
    if player.pos()[1] < -280:
        player.setheading(90)

    if player.pos()[1] < tager.pos()[1] + 5 and player.pos()[1] > tager.pos()[1] - 5:
        if player.pos()[0] < tager.pos()[0] + 5 and player.pos()[0] > tager.pos()[0] - 5:
            turtle.goto(0, 50)
            turtle.color("red")
            turtle.write("Game Over", align="center", font=("arial", 25, "bold"))
            playing = False
