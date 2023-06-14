import turtle

from itertools import cycle
colors = cycle(['red','orange','yellow','green','blue','purple'])


def draw_shape(size,angle,shift,shape):
    turtle.pencolor(next(colors))
    next_shape =11
    if shape =='circle':
        turtle.circle(size)
        next_shape = 'circle'
    elif shape =='circle':
        for l in range(4):
            turtle.forward(size+2)
            turtle.left(90)
        next_shape = 'circle'
    turtle.right(angle)
    turtle.forward(shift)
    draw_shape(size+5,angle+20,shift+10)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_shape(30,0,1,'circle')
                    
