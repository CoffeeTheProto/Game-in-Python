import turtle as t
t.speed(0)
window_height = t.window_height()
window_width = t.window_width()
def hallT():
    t.clear()
    #Draw the left side
    t.pu()
    t.setpos(-275,-(window_height / 2))
    t.seth(70)
    t.pd()
    t.fd(300)
    t.lt(20)
    t.fd(350)
    t.lt(100)
    t.fd(300)
    #Draw the right side
    t.pu()
    t.setpos(275,-315)
    t.seth(110)
    t.pd()
    t.fd(300)
    t.rt(20)
    t.fd(350)
    t.rt(100)
    t.fd(300)

def hallL():
    t.clear()
    #Draw the left side
    t.pu()
    t.setpos(-275,-(window_height / 2))
    t.seth(70)
    t.pd()
    t.fd(300)
    t.lt(20)
    t.fd(200)
    t.fd(150)
    t.lt(100)
    t.fd(300)
    #Draw the right side
    t.pu()
    t.setpos(275,-315)
    t.seth(110)
    t.pd()
    t.fd(450)
    t.lt(70)
    t.fd(294)
    t.pu()
    t.bk(294)
    t.rt(90)
    t.pd()
    t.fd(250)
    t.rt(100)
    t.fd(400)
    t.bk(400)
    t.lt(190)
    t.fd(600)

def hallR():
    t.clear()
    #Draw the right side
    t.pu()
    t.setpos(275,-(window_height / 2))
    t.seth(110)
    t.pd()
    t.fd(300)
    t.rt(20)
    t.fd(200)
    t.fd(150)
    t.rt(100)
    t.fd(300)
    #Draw the left side
    t.pu()
    t.setpos(-275,-315)
    t.seth(70)
    t.pd()
    t.fd(450)
    t.rt(70)
    t.fd(294)
    t.pu()
    t.bk(294)
    t.lt(90)
    t.pd()
    t.fd(250)
    t.lt(110)
    t.fd(400)
    t.bk(400)
    t.rt(200)
    t.fd(600)

