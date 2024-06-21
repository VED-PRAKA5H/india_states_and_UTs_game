import pandas as pd
import turtle
from score_board import Score
import time
from turtle import Turtle, Screen

# screen setup
screen = Screen()
screen.setup(700, 700)
screen.bgpic('bharat.gif')

# register a shape in turtle
image = 'bharat.gif'
screen.addshape(image)
# turtle.shape(image)
# screen.tracer(1)

# creating turtle object
turtle_obj = Turtle()
turtle_obj.penup()
turtle_obj.hideturtle()


# screen.listen()
# def up():
#     turtle_obj.setheading(90)
#     turtle_obj.forward(20)
#
# def down():
#     turtle_obj.setheading(270)
#     turtle_obj.forward(20)
# def forward():
#     turtle_obj.setheading(0)
#     turtle_obj.forward(20)
#
# def backward():
#     turtle_obj.setheading(180)
#     turtle_obj.forward(20)
#
#

# x = [-55.0, 179.0, 47.0, -11.0, -136.0, -164.0, -92.0, -80.0, 38.0, -107.0, -97.0, 151.0, -71.0, -115.0, 169.0, 135.0,
#      158.0, 178.0, 30.0, -107.0, -135.0, 87.0, -69.0, -58.0, 138.0, -50.0, -31.0, 80.0, 174.0, -95.0, [-149.0,
#      -168.0], -80.0, -115.0, -81.0, -166.0, -43.0]
# y = [-143.0, 95.0, 42.0, -31.0, -128.0, -2.0, 98.0, 144.0, 3.0, -143.0, -217.0, 57.0, -3.0, -61.0, 33.0, 44.0, 11.0,
#      61.0, -41.0, 129.0, 54.0, 72.0, -212.0, -93.0, 13.0, 112.0, 58.0, 2.0, -189.0, 125.0, [-47.0, -33.0], 90.0,
#      172.0, 189.0, -197.0, -193.0]
# turtle_obj.shape('turtle')
df = pd.read_csv('36_states_UTs.csv')
# df['X'] = x
# df['Y'] = y
# df.to_csv('36_states_UTs.csv')
x = df.X
y = df.Y
su = df.States_and_Uts

score = Score()


def show_states_name(i):

    if su[i] == 'Dadra and Nagar Haveli and Daman and Diu'.title():
        """this location has multiple places that is x and y coord are in string that contains a list
            first we remove square bracket by strip method and then we make this string into list using
             split method separated by ',' """
        X = x[i].strip('[]').split(',')
        Y = y[i].strip('[]').split(',')
        turtle_obj.goto(float(X[0]), float(Y[0]))
        turtle_obj.write('Dadra and Nagar Haveli and Daman')
        turtle_obj.forward(168)
        turtle_obj.pendown()
        turtle_obj.dot()
        turtle_obj.penup()
        turtle_obj.goto(float(X[1]), float(Y[1]))
        turtle_obj.write('Diu')
        turtle_obj.pendown()
        turtle_obj.dot()
        turtle_obj.penup()
    else:
        turtle_obj.goto(float(x[i]), float(y[i]))
        turtle_obj.pendown()
        turtle_obj.dot()
        turtle_obj.penup()
        turtle_obj.write(su[i])

answered = []
tic = time.time()
game_is_on = True
while game_is_on:
    answer = screen.textinput('Guess the State or UT name', 'what is another name?')

    states_uts = df.States_and_Uts
    states_uts_list = states_uts.to_list()

    if answer.title() in states_uts_list and answer.title() not in answered:
        position_of_states = states_uts_list.index(answer.title())
        show_states_name(position_of_states)
        answered.append(answer.title())

    if int((time.time()-tic)/60) == 1:
        game_is_on = False
    score.show_score(len(answered), time.time()-tic)



#     screen.update()
#     time.sleep(0.1)
#     screen.onkey(down, 'Down')
#     screen.onkey(up, 'Up')
#     screen.onkey(fun=forward, key='Right')
#     screen.onkey(backward, 'Left')
# screen.exitonclick()
turtle.mainloop()

