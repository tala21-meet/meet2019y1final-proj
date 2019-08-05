import turtle #listening (keypress)
def up():
    turtle.goto(turtle.xcor(),turtle.ycor()+100)
def down():
    turtle.goto(turtle.xcor(),turtle.ycor()-100)
def right():
    turtle.goto(turtle.xcor()+100,turtle.y())



turtle.onkeypress(up,'Up')
turtle.onkeypress(down,'Down')
turtle.onkeypress(Right,'Right')

turtle.listen()
when 
if len(health)>=80:
    print('you are super healthy!')
elif len(health)>=50:
    print('your health is struggling!')
elif len(health)>=10:
    print('you are dying!!!!')
if len(environment)>=80:
    print('what a green environment that U live in!!!')
elif len(environment)>=50:
    print('this environment is okay...')
elif len(environment)>=10:
    print('what a dirty environment!!!')
if len(energy)>=80:
    print('what a great energy!!')
elif len(energy)>=50:
    print('your energy is okay...)
elif len(energy)>=10:
    print('your energy is tooo low!!)
