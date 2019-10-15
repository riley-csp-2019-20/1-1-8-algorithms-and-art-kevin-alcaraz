import turtle as trtl
juan = trtl.Turtle()

wn = trtl.Screen()
wn.bgcolor("skyblue")

juan.right(135)
juan.circle(70,280)
juan.right(90)
juan.circle(50)

juan.penup()
juan.goto(25,-25)
juan.begin_fill()
juan.pendown()
juan.circle(5)
juan.end_fill()

juan.penup()
juan.begin_fill()
juan.goto(20,-50)
juan.pendown()
juan.circle(5)
juan.end_fill()

juan.penup()
juan.begin_fill()
juan.goto(25,-75)
juan.pendown()
juan.circle(5)
juan.end_fill()


























wn.mainloop()