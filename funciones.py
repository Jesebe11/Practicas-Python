import turtle

def main():
     window = turtle.Screen()
     jesebell = turtle.Turtle()

     make_square(jesebell)

     turtle.mainloop()

def make_square(jesebell):
    length = int(input('Tamaño de cuadrado : '))

    for i in range(4):
        make_line_and_turn(jesebell, length)

def make_line_and_turn(jesebell, length):
        jesebell.forward(length)
        jesebell.left(90)

if __name__ == "__main__":
    main()
