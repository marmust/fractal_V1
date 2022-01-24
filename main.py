import turtle
x = 0
y = 0
rotation = int(input("rotation speed (def: 5): "))
while True:
    turtle.speed(0)
    turtle.forward(3 + y)
    turtle.right(x * 10)
    x = x + 1
    y = y + 0.1
    turtle.right(rotation)