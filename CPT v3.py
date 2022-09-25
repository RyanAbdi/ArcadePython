# Created By Ryan Abdi
# last changed Sept 25 2022
# Grade 10 CPT
# Multiple games in one code


import turtle
import time
import random
import tkinter
import webbrowser

global outputs



def agains():  # This is the main menu function

    menu = tkinter.Tk()
    menu.title("Main Menu")
    menu.geometry("500x500")
    menu.resizable(False,False)

    def instructions():
        webbrowser.open("https://www.wikihow.com/Play-Rock,-Paper,-Scissors")
        webbrowser.open("https://www3.nd.edu/~lemmon/courses/ee224/web-manual/web-manual/lab6/node4.html")
        webbrowser.open("https://www.wikihow.com/Play-Ping-Pong-(Table-Tennis)")

    outputs = "Welcome to my Grade 10 ComSci CPT"

    Welcome = tkinter.Label(menu, text=outputs, fg="red", bg="black", font="Arial, 20", width=100, height=8)


    RPS = tkinter.Button(menu, text="Rock Paper Scissors", fg="black", bg="grey", font="Arial,15", padx=10, pady=10, command=rock,
                          width=100)

    GTN = tkinter.Button(menu, text="Guess The Number", fg="black", bg="white", font="Arial,15", padx=10, pady=10, command=number,
                           width=100)
    PONG = tkinter.Button(menu, text="Pong", bg="cyan", fg="black", font="Arial,15", padx=10, pady=10,
                              command=pong, width=100)
    Instructions = tkinter.Button(menu, text="Instructions", fg="yellow", bg="black", font="Arial 20",
                            command=lambda:[instructions(), Welcome.config(text="Guess the Number: played in terminal\nPong: Player 1 uses W and S\nPlayer 2 uses arrow keys")], width=100, height=1)
    fullquit = tkinter.Button(menu, text="Quit", fg="yellow", bg="black", font="Arial 20", command=quit, width=100,
                              height=1)

    Welcome.pack()  # This packs the code into the menu
    RPS.pack()
    GTN.pack()
    PONG.pack()
    Instructions.pack()
    fullquit.pack()

    menu.call('wm', 'attributes', '.', '-topmost', '1')
    menu.mainloop()  # this keeps the window open until closed




def rock():  # Rock paper Scissors game
    stats = []

    def user(user_input):
        num = random.randint(1, 3)  # Creates a random integer
        if num == 1:
            computer = "rock"
        elif num == 2:
            computer = "scissors"
        else:
            computer = "paper"

        if (computer == "rock" and user_input == "paper") or (computer == "paper" and user_input == "scissors") or (computer == "scissors" and user_input == "rock"):  # These are the win conditions
            stats.append('W')
            result = "You won!"
        elif computer == user_input:
            stats.append('T')
            result = "It's a tie"
        else:
            stats.append('L')
            result = "You lost!"

        output.config(text="Computer chose: " + computer + "\n" + "You chose: " + user_input + "\n" + result)

    def scissors():
        user("scissors")

    def rock():
        user("rock")

    def paper():
        user("paper")

    def end():
        if stats.count('L') > stats.count('W'):
            result = "\nYou loose the series."
        elif stats.count('L') == stats.count('W'):
            result = "\nSeries ended in a draw."
        else:
            result = "\nYou win the series."
        root1 = tkinter.Tk()
        root1.title("Results")
        root1.geometry("500x500")
        root1.config(bg="Black")
        root1.attributes('-topmost', True)

        res = tkinter.Label(root1, text=result, fg="red", bg="black", font="Arial 30")
        res.pack()
        history = tkinter.Label(root1, text="\n \n The match history is: \n", fg="red", bg="black", font="Arial 30")
        history.pack()
        results = tkinter.Label(root1, text=stats, fg="red", bg="black", font="Arial 30")
        results.pack()
        quitss = tkinter.Button(root1, text="Exit", fg="red", bg="black", font="Aral, 30",
                                command=root1.destroy)
        quitss.pack(side="bottom")

        root1.after(3000, root1.destroy)

        root.destroy()

    # This opens the window
    root = tkinter.Tk()
    root.title("Rock, paper scissors")
    root.geometry("500x500")

    # This creates all the buttons
    rock = tkinter.Button(root, text="Rock", fg="black", bg="grey", font="Arial,12", padx=10, pady=5, command=rock,width=100)
    paper = tkinter.Button(root, text="Paper", fg="black", bg="white", font="Arial,12", padx=10, pady=5, command=paper,width=100)
    scissors = tkinter.Button(root, text="Scissors", bg="cyan", fg="black", font="Arial,12", padx=10, pady=5, command=scissors, width=100)
    output = tkinter.Label(root, text="Click a button", fg="red", bg="black", font="Arial, 25", width=100, height=7)
    goback = tkinter.Button(root, text="Click to go back to the main menu", fg="yellow", bg="black", font="Arial 20", command=end, width=100, height=1)
    fullquit = tkinter.Button(root, text="Quit", fg="yellow", bg="black", font="Arial 20", command=quit, width=100, height=1)

    rock.pack()   # This packs the code into the menu
    paper.pack()
    scissors.pack()
    output.pack()
    goback.pack()
    fullquit.pack()
    root.call('wm', 'attributes', '.', '-topmost', '1')
    root.mainloop()  # this keeps the window open until closed



def number():  # guess the number game
    guess = ""
    guess_count = 0
    guess_limit = 7
    print("You have 7 of guesses to guess the right number")
    num = random.randint(1, 100)  # Creates a random number for the user to guess
    while guess != num and guess_count < guess_limit:
        guess = int(input("Pick a number between 1 and 100: "))
        if guess > 100 or guess < 0: # If the user guesses over 100 or below zero the guess wont count
            print("the number is between 1 and 100 try again")
            guess_count -= 1
        guess_count += 1
        if guess == num and guess_count <= guess_limit:
            print("Nice You won! \nHint 2:_ _ 06 _ 3")
            
        elif guess != num and guess_count != 0 and guess > 0 and guess < 100:
            print("Nice try but you are wrong, you have", guess_limit-guess_count, "guesses left")
            if num > guess:  # if the random number is greater than the guessed the number this will print that your guess was too low
                print("Too low")
            if num < guess:
                print("Too high")
        if guess_count >= guess_limit:
            print("Uh oh, you are out of guesses, Game over, the number was", num, "\nPlease Return to main menu")



def pong():     # pong game
    Gameover = False

    wn = turtle.Screen()  # creates the pong window
    wn.title("Ping pong but on the computer")  # This sets the title window to "Ping pong but on the computer
    wn.bgcolor("black")  # This makes the background color of the screen black
    wn.setup(width=800, height=600)
    wn.tracer(0)

    rootwindow = wn.getcanvas().winfo_toplevel()  # This makes the window pop on top of everything else
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

    score1 = 0
    score2 = 0

    ball = turtle.Turtle()  # This creates the ball
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = .25
    ball.dy = -.25

    pen = turtle.Turtle()  # This writes the player1 and player 2 at the top of the screen
    pen.speed(0)
    pen.color("yellow")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player 1: 0          Player 2: 0", align="center", font=("arial", 24, "normal"))

    paddle1 = turtle.Turtle()  # This creates the paddle 1
    paddle1.speed(0)
    paddle1.shape("square")
    paddle1.color("red")
    paddle1.shapesize(stretch_wid=5, stretch_len=1)
    paddle1.penup()
    paddle1.goto(-350, 0)

    paddle2 = turtle.Turtle()  # This creates Paddle 2
    paddle2.speed(0)
    paddle2.shape("square")
    paddle2.color("blue")
    paddle2.shapesize(stretch_wid=5, stretch_len=1)
    paddle2.penup()
    paddle2.goto(350, 0)

    def paddle1up():
        y = paddle1.ycor()
        y += 30
        paddle1.sety(y)

    def paddle1down():
        y = paddle1.ycor()
        y -= 30
        paddle1.sety(y)

    def paddle2up():
        y = paddle2.ycor()
        y += 30
        paddle2.sety(y)

    def paddle2down():
        y = paddle2.ycor()
        y -= 30
        paddle2.sety(y)
    # This detects keyboard input
    wn.listen()
    wn.onkeypress(paddle1up, "w")
    wn.onkeypress(paddle1down, "s")
    wn.onkeypress(paddle2up, "Up")
    wn.onkeypress(paddle2down, "Down")

    time.sleep(1.5)


    while Gameover != True:  # this is the main game loop
        wn.update()  # updates the turtle screen
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if paddle1.ycor() > 290:  # This stops the paddle from going off screen
            paddle1.sety(290)

        if paddle1.ycor() < -290:
            paddle1.sety(-290)

        if paddle2.ycor() > 290:
            paddle2.sety(290)

        if paddle2.ycor() < -290:
            paddle2.sety(-290)

        if ball.ycor() > 290:  # This switches the balls direction if it hits a wall
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:  # this resets the ball if someone has scored
            ball.goto(0, 0)
            ball.dx *= -1
            score1 += 1
            pen.clear()
            pen.write("Player 1: {}          Player 2: {}".format(score1, score2), align="center", font=("arial", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score2 += 1
            pen.clear()
            pen.write("Player 1: {}          Player 2: {}".format(score1, score2), align="center", font=("arial", 24, "normal"))

        if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40): #  This detects if the ball hits the paddle
            ball.setx(-340)
            ball.dx *= -1

        if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1

        if score1 == 5 or score2 == 5:  # This detects if the one player wins
            global outputs
            pen.clear()
            if score1 == 5:
                pen.write("Player 1 wins", align="center", font=("arial", 30, "bold"))
                outputs = "Player 1 wins"
            if score2 == 5:
                pen.write("Player 2 wins ", align="center", font=("arial", 30, "bold"))
                outputs = "Player 2 wins"
            pen.penup()
            pen.goto(0, 0)
            pen.pendown()
            pen.write("The game will close in 5 seconds", align="center", font=("arial", 30, "bold"))
            time.sleep(5)
            Gameover = True


    wn.bye()
    turtle.Turtle._screen = None  # force recreation of singleton Screen object
    turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition





agains()
