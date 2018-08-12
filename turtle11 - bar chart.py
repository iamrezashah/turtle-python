import turtle

# 1 -important- to create main window or frame
main_window = turtle.Screen()

# 2 -important- to create turtle
little_turtle = turtle.Turtle()

# optional attributes =========================
main_window.bgcolor("lightgray")
little_turtle.speed(10)
little_turtle.pensize(2)
little_turtle.color('green', 'gray')  # 1: pen color     2: filling color
# 3 end========================================
x, y = -300, 0  # start point


def draw_1_bar(turtle, height):
    global x
    global y

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.begin_fill()  # *** start filling area
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(height)

    # ===============================================================================
    # turtle.write(arg, move=False, align="left", font=("Arial", 8, "normal"))
    # Parameters:
    #   arg – object to be written to the TurtleScreen
    #   move – True/False
    #   align – one of the strings “left”, “center” or right”
    #   font – a triple (fontname, fontsize, fonttype)
    turtle.color('red', 'gray')  # change font color but filling color
    turtle.write(height, False, 'left', font=("Arial", 15, "normal"))
    turtle.color('green', 'gray')  # return / change font color but filling color
    # ===============================================================================

    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(10)
    turtle.end_fill()   # *** end filling area

    x, y = turtle.position()  # current pen's position


bars = [20, -180, 135, 60, 210, -100, 58, 98, 24, 70]


for each_height in bars:
    draw_1_bar(little_turtle, each_height)

# 3 -important- fa: bad az rasme shekl, window baste nashe
main_window.mainloop()