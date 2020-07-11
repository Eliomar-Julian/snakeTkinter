from tkinter import *
from random import (choice)
from PIL import Image, ImageTk

SIZE = 20
KEY = str("")
EX, EY = 0, 0
DELAY = 100
SNAKE = []
COORD = []


class Jogo:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x500+400+100")
        self.window.bind("<KeyPress>", self.keypress)
        self.map()

    def map(self):
        self.mapa = Frame(
            self.window, width=500, height=500, bg="teal"
        )
        self.mapa.pack(expand=True)
        self.snake()
        self.place()
        self.food()
        self.loop()

    def keypress(self, key):
        global KEY
        KEY = key.keysym

    def move(self):
        global EX, EY
        if KEY == "Right":
            EX = EX + SIZE
        elif KEY == "Left":
            EX = EX - SIZE
        elif KEY == "Up":
            EY = EY - SIZE
        elif KEY == "Down":
            EY = EY + SIZE
        self.cobra.place(x=EX, y=EY)

    def snake(self):
        self.cobra = Frame(
            self.mapa, width=SIZE, height=SIZE, bg="white"
        )
        self.cobra.place(x=0, y=0)

    def place(self):
        lis = []
        for k in range(0, 500 - SIZE, SIZE):
            lis.append(k)
        self.x = choice(lis)
        self.y = choice(lis)

    def food(self):
        cor = [
            "white", "gray", "black",
            "pink", "blue", "purple",
            "red", "violet", "yellow"
        ]
        self.fruit = Frame(
            self.mapa, width=SIZE, height=SIZE, bg=choice(cor)
        )
        self.fruit.place(x=self.x, y=self.y)

    def collision(self):
        if EX < 0 or EX > 500 - SIZE:
            return "saiu"
        if EY < 0 or EY > 500 - SIZE:
            return "saiu"
        if EX == self.x and EY == self.y:
            return "comeu"
        tup = tuple((EX, EY))
        if tup in COORD:
            return "morreu"

    def game_over(self):
        self.texto = Label(
            self.mapa, fg="red", text="Fim de Jogo",
            font=("Arial", 50, "bold"), bg="teal"
        )
        self.pontos = Label(
            self.mapa, fg="blue", text="Pontos: " +
            str(len(SNAKE) * 5) + "\nTamanho: " + str(len(SNAKE)),
            font=("Arial", 30, "bold"), bg="teal",
        )
        self.bt = Button(
            self.mapa, text="Jogar Novamente", relief="flat",
            cursor="exchange", font=("Arial", 20, "bold"),
            fg="blue", bg="green", command=self.clear
        )
        self.texto.place(relx=0.1, rely=0.1)
        self.pontos.place(relx=0.3, rely=0.3)
        self.bt.place(relx=0.25, rely=0.5)

    def clear(self):
        global EX, EY, SNAKE, COORD, KEY
        EX, EY, KEY = 0, 0, ""
        SNAKE, COORD = [], []
        for k in [
            self.mapa, self.fruit,
            self.texto, self.pontos,
            self.cobra
        ]:
            k.destroy()
        self.map()
        return

    def loop(self):
        global SNAKE, COORD
        colisao = self.collision()
        if colisao == "saiu":
            self.game_over()
            return
        if colisao == "comeu":
            self.fruit.destroy()
            self.place()
            self.food()
            SNAKE.append(Frame(self.mapa, width=SIZE, height=SIZE, bg="white"))
        if colisao == "morreu":
            self.game_over()
            return

        COORD.append((EX, EY))
        if len(COORD) > len(SNAKE):
            del(COORD[0])

        diminu = len(SNAKE)
        for self.k in SNAKE:
            self.k.place(x=COORD[-diminu][0], y=COORD[-diminu][1])
            diminu = diminu - 1

        self.move()
        self.window.after(DELAY, self.loop)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    snake = Jogo()
    snake.run()
