
import turtle
t = turtle.Turtle()
t.speed(123456789)
turtle.bgcolor("black")
colors = ["Red","Orange","Yellow","Green","Blue","Purple"]

yourname = turtle.textinput(
    "enter ur name", "what is ur name")

for x in range(100):
    t.color( colors[x % 6 ] )
    t.up()
    t.forward(x*4)
    t.down()
    t.write (yourname, font = ("Arial",int( (x + 6) / 6), "bold"))
    t.left(60)
