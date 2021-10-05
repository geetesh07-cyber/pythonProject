from turtle import Turtle,Screen
import turtle
import random
turtle.colormode(255)
timmy = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.fd(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.fd(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.fd(100)
# timmy_the_turtle.right(90)
#timmy_the_turtle.fd(100)
#we can do this by while loop alse but problem is it's keep moving

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range(10):
#      if _ % 2 == 0:
#          timmy.color("white")
#          timmy.forward(15)
#      timmy.color("black")
#      timmy.forward(15)
#we can use pen up and pen down functionn to create dash lines
# for _ in range (15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

#
# #DRAW SHAPES BASICS FROM 3 SIDES TO 10 SIDED
# colours = ["red","magenta1","maroon","purple","hotpink","lawngreen","yellow","firebrick1","CadetBlue1","DarkBlue","cyan",
#            "magenta4","OrangeRed"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     colour = colours[num_sides-3]
#     timmy.color(colour)
#     for sides in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#now to add colours
# sides = 3
condition = True
angles = [0,90,180,270]
# while condition:
#     draw_shape(sides)
#     sides += 1
#     if sides > 10 :
#         condition = False

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_tuple = (r,g,b)
    return my_tuple
timmy.width(5)
timmy.speed("fastest")
count = 1
# while condition:
#     colour = random_color()
#     timmy.color(colour)
#     timmy.forward(100)
#     timmy.setheading(random.choice(angles))
#     count += 1
#     if count>200 :
#         condition = False


#challenge 5
#create a spirograph
while condition:
    colour = random_color()
    timmy.color(colour)
    timmy.circle(100)
    count += 1
    if count > 35:
        condition = False
    current_heading = timmy.heading()
    timmy.setheading(current_heading + 10)



screen = Screen()
# screen.bgcolor("blue")
screen.exitonclick()
