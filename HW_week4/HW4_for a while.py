from turtle import *
import random


bgcolor("black")
pencolor("deepPink")



for i in range (10):
    penup()
    goto(random.randint(-400, 400), random.randint (-400, 400))
    pendown()
    speed(0)
    a = random.randint(0, 4)
    b = random.randint(0, 4)
    while True:
        forward(a)
        right(b)
        a+=2
        b+=1
        if b == 200:
            break

