import turtle

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(40)
turtle.pencolor('red')
turtle.circle(30)
def draw_circle(size):
    turtle.pencolor('red')
    turtle.circle(size)
    draw_circle(size)

    turtle.bgcoloe('black')
    turtle.speed('fast')
    turtle.pensize(4)
    draw_circle(30)

    import turtle

    from itertools import cycle
    colors = cycle({'red', 'orange', 'yellow', 'green', 'blue', 'purple'})
    def draw_circle(size):
        turtle.pencolor(next(colors))
        turtle.circle(size)
        draw_circle(size+5)

    turtle.bgcolor('black')
    turtle.speed('fast')
    turtle.pensize(4)
    draw_circle(30)

    import turtle

    from itertools import cycle
    colors = cycle(['red','orangr','yellow','green','biue','purple'])

    def draw_circle(size,angle,shift):
        turtle.pencolor(next(colors))
        turtle.circle(size)
        turtle.fight(angle)
        turtle.forward(shift)
        draw_circle(size+5,angle+1,shift+1)
        turtle.bgcolor('black')
        turtle.speed('fast')
        turtle.pensize(4)
        draw_circle(30,0,1)

        import turtle

        from itertools import cycle
        colors = cycle(['red','orange','yellow','yellow','green','blue','purple'])

        def draw_circle(size,angle,shift):
            turtle.bgcolor(next(colors))
            turtle.pencolor(next(colors))
            turtle.circle(size)
            turtle.right(angle)
            turtle.forward(shift)
            draw_circle(size+5,angle+1,shift+1)

            turtle.bgcolor('black')
            turtle.speen('fast')
            turtle.pensize(40)
            draw_circle(30,0,1)

































        


        

    
    
                    
    
    
    

