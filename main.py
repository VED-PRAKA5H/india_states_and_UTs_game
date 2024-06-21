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


# creating turtle object
turtle_obj = Turtle()
turtle_obj.penup()
turtle_obj.hideturtle()

df = pd.read_csv('36_states_UTs.csv')

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



turtle.mainloop()

