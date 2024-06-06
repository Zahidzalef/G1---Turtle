import random
import turtle

ekran = turtle.Screen()
oyun_bitti = False
skor = 0
FONT = ("Arial", 25, "normal")

turtle_liste = []
geri_sayim_turtle = turtle.Turtle()
skor_turtle = turtle.Turtle()
boyut = 10

x_koordinat = [-20, -10, 0, 10, 20]
y_koordinat = [20, 10, 0, -10]


def skor_kurulum_turtle():
    skor_turtle.hideturtle()
    skor_turtle.color("blue")
    skor_turtle.penup()
    top_heigh = ekran.window_height() / 2
    y = top_heigh - top_heigh / 10
    skor_turtle.setposition(0, y)
    skor_turtle.write(arg="Skor : 0", move=False, align="center", font=FONT)


def yap_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global skor
        skor += + 1
        skor_turtle.clear()
        skor_turtle.write("Score : {}".format(skor), move=False, align="center", font=FONT)
        print(x, y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.goto(x * boyut, y * boyut)
    t.pendown()
    turtle_liste.append(t)


def kurulum_turtles():
    for x in x_koordinat:
        for y in y_koordinat:
            yap_turtle(x, y)


def sakla_turtles():
    for t in turtle_liste:
        t.hideturtle()


def random_gosterme_turtle():
    if not oyun_bitti:
        sakla_turtles()
        random.choice(turtle_liste).showturtle()
        ekran.ontimer(random_gosterme_turtle, 500)


def say(time):
    global oyun_bitti
    top_height = ekran.window_height() / 2
    y = top_height - top_height / 10
    geri_sayim_turtle.hideturtle()
    geri_sayim_turtle.penup()
    geri_sayim_turtle.setposition(0, y - 30)
    geri_sayim_turtle.clear()
    if time > 0:
        geri_sayim_turtle.clear()
        geri_sayim_turtle.write("Zaman : {}".format(time), move=False, align="center", font=FONT)
        ekran.ontimer(lambda: say(time - 1), 1000)
    else:
        oyun_bitti = True
        geri_sayim_turtle.clear()
        sakla_turtles()
        geri_sayim_turtle.write("OYUN BİTTİ!", align="center", font=FONT)


def baslatici():
    global oyun_bitti
    oyun_bitti = False
    turtle.tracer(0)
    skor_kurulum_turtle()
    kurulum_turtles()
    sakla_turtles()
    random_gosterme_turtle()
    turtle.tracer(1)
    ekran.ontimer(lambda: say(10), 10)


baslatici()
turtle.mainloop()
