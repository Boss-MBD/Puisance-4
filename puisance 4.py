# ---------- ---------- setup

print("-----")
print("-----")
from turtle import *
import turtle as tur
print("-")
#Screen().tracer(0)
hecran = 1080
lecran = 1920
setup(lecran, hecran)
bgcolor("black")
title("lancé de dés")
#exitonclick()
color("white")
width(1)
speed(0)
tur.shape('turtle')

screen = Screen()
screen.setup(200, 200, 0, 0)

#---------- ---------- définitions

tab = [[], [], [], [], [], [], []]
couleur = 0
full = 0
turn = "R"

#---------- ---------- tracé du plateau

color("blue")
up()
goto(-525, -450)
down()
begin_fill()
for i in range(2):
    forward(1050)
    left(90)
    forward(900)
    left(90)
end_fill()

up()
color("black")
for i in range(6):
    for j in range(7):
        goto(-450 + (150 * j), -375 + (150 * i))
        dot(125)

color("white")
goto(-450, -525)
for i in range(7):
    write(i+1, font=('Arial',20,'bold'))
    forward(150)

#---------- ---------- Victoire

def victoire():
    if turn == "R":
        goto(-100, 0)
        color("red")
        down()
        width(120)
        goto(100, 0)
        goto(0, 0)
        write("Rouge a gagné", font=('Arial',100,'bold'))


    elif turn == "Y":
        goto(-100, 0)
        color("yellow")
        down()
        width(120)
        goto(100, 0)
        goto(0, 0)
        write("jaune a gagné", font=('Arial',100,'bold'))
    
    done()

#---------- ---------- console

for i in range(100000):

#---------- Choix de la couleur

    if couleur % 2 == 0:
        color("red")
        turn = "R"
    elif couleur % 2 == 1:
        color("yellow")
        turn = "Y"

#---------- Input

    placex = textinput("Conect four", "Enter the row you wants to play in")
    if placex.isnumeric():
        placex = int(placex)
        placey = len(tab[placex - 1])
        if placey < 6:
            couleur = couleur + 1
            full = full + 1
            goto(-600 + (150 * placex), -375 + (150 * placey))
            dot(125)

#---------- Insertion dans le tableau

            if couleur % 2 == 0:
                tab[placex - 1].append("R")
            elif couleur % 2 == 1:
                tab[placex - 1].append("Y")

#---------- Condition de victoire
'''
# ligne
            placey = placey + 1
            if tab[placex + 2][placey] == turn and tab[placex + 1][placey] == turn and tab[placex][placey] == turn:
                victoire()
            elif tab[placex - 2][placey] == turn and tab[placex][placey] == turn and tab[placex + 1][placey] == turn:
                victoire()
            elif tab[placex][placey - 2] == turn and tab[placex - 3][placey] == turn and tab[placex][placey] == turn:
                victoire()
            elif tab[placex - 2][placey] == turn and tab[placex - 3][placey] == turn and tab[placex - 4][placey] == turn:
                victoire()


# colonne
            placey = placey - 1
            placex = placex + 1
            if tab[placex][placey] == turn and tab[placex][placey + 1] == turn and tab[placex][placey + 2] == turn:
                victoire()
            elif tab[placex][placey] == turn and tab[placex][placey + 1] == turn and tab[placex][placey - 2] == turn:
                victoire()
            elif tab[placex][placey] == turn and tab[placex][placey - 2] == turn and tab[placex][placey - 3] == turn:
                victoire()
            elif tab[placex][placey - 2] == turn and tab[placex][placey - 3] == turn and tab[placex][placey - 4] == turn:
                victoire()

# diagonale droite
            placex = placex - 1
            if tab[placex][placey] == turn and tab[placex + 1][placey + 1] == turn and tab[placex + 2][placey + 2] == turn:
                victoire()
            elif tab[placex][placey] == turn and tab[placex + 1][placey + 1] == turn and tab[placex - 2][placey - 2] == turn:
                victoire()
            elif tab[placex][placey] == turn and tab[placex - 2][placey - 2] == turn and tab[placex - 3][placey - 3] == turn:
                victoire()
            elif tab[placex - 2][placey - 2] == turn and tab[placex - 3][placey - 3] == turn and tab[placex - 4][placey - 4] == turn:
                victoire()


# diagonale gauche

            if tab[placex - 2][placey] == turn and tab[placex - 3][placey + 1] == turn and tab[placex - 4][placey + 2] == turn:
                victoire()
            elif tab[placex - 2][placey] == turn and tab[placex - 3][placey + 1] == turn and tab[placex][placey - 2] == turn:
                victoire()
            elif tab[placex - 2][placey] == turn and tab[placex][placey - 2] == turn and tab[placex + 1][placey - 3] == turn:
                victoire()
            elif tab[placex][placey - 2] == turn and tab[placex + 1][placey - 3] == turn and tab[placex + 2][placey - 4] == turn:
                victoire()

# Egalité

            if full == 42:
                goto(-220, -50)
                down()
                color("white")
                write("Egalité", font=('Arial',100,'bold'))
                hideturtle()
                done()

#---------- Colonne pleine

        else:
            placex = textinput("Conect four", "Enter a row that isn't full! (Just say anything, it's a popup)")
    else:
        placex = textinput("Conect four", "Please enter a number! (Just say anything, it's a popup)")
'''
#---------- ---------- fin

#Screen().update()
done()