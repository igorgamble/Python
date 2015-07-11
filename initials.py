import turtle

def draw_line(some_turtle):
    for i in range(1,2):
        some_turtle.left(90)
        some_turtle.forward(100)
        
        

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(1)
    for i in range (1,2):
        draw_line(brad)
        

    angie = turtle.Turtle()
    angie.goto(60,0)
    angie.shape("turtle")
    angie.color("black")
    angie.left(90)
    angie.forward(100)
    angie.right(90)
    angie.forward(60)
    angie.right (90)
    angie.forward(10)

    edie = turtle.Turtle()
    edie.goto(60,0)
    edie.shape("turtle")
    edie.color("black")
    edie.forward(60)
    edie.left(90)
    edie.forward(30)
    edie.left(90)
    edie.forward(15)
    edie.left(90)
    edie.forward(5)

    window.exitonclick()

draw_art()
