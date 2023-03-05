import turtle
tartaruga = turtle.Turtle()
tartaruga.speed(0)
tartaruga.pensize(3)

# Desenhar o escudo do Superman
tartaruga.penup()
tartaruga.goto(0, -150)
tartaruga.pendown()
tartaruga.begin_fill()
tartaruga.color("#ff0000", "#ff0000") # vermelho
for _ in range(3):
    tartaruga.forward(200)
    tartaruga.left(120)
tartaruga.end_fill()

tartaruga.penup()
tartaruga.goto(0, -50)
tartaruga.pendown()
tartaruga.begin_fill()
tartaruga.color("#ffff00", "#ffff00") # amarelo
for _ in range(3):
    tartaruga.forward(80)
    tartaruga.left(120)
tartaruga.end_fill()

tartaruga.penup()
tartaruga.goto(0, 50)
tartaruga.pendown()
tartaruga.begin_fill()
tartaruga.color("#0000ff", "#0000ff") # azul
for _ in range(3):
    tartaruga.forward(80)
    tartaruga.left(120)
tartaruga.end_fill()

janela = turtle.Screen()
janela.bgcolor("#ffffff") # branco
janela.mainloop()
