from tkinter import (Tk, Frame, Label, Button)
from random import (randint, choice)
from time import sleep

# -- Configurações --
DELAY = 100
KEY = "Right"
MX = 0
MY = 0
SNAKE = []
COORD = []
PASSO = 15
PONTOS = 0


class Game:
    def __init__(self):
        self.window = Tk()
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.XX, self.YY = 500, 500
        self.window.geometry(
            f"{self.XX}x{self.YY}+{(width - self.XX) // 2}+{(height - self.YY) // 2}")
        self.window.resizable(0, 0)
        self.window.bind("<KeyPress>", self.keypress)

        self.body()

    def body(self):
        self.table = Frame(self.window, width=self.XX,
                           height=self.YY, bg="#4A5B00")
        self.table.pack(expand=True)

        self.head()
        self.food()
        self.loop()

    def head(self):
        self.cabeca = Frame(self.table, width=PASSO, height=PASSO, bg="white")
        self.cabeca.place(x=0, y=0)

    def food(self):
        cor = ["white", "black", "orange", "yellow", "purple",
               "violet", "gray", "green", "teal", "blue", "#cc0099",
               "#ff4000", "#cc5200", "#8c66ff", "#1affff", "#70db70"]
        self.comida = Frame(self.table, width=PASSO,
                            height=PASSO, bg=str(choice(cor)))
        lis = []
        for k in range(0, (self.XX - PASSO), PASSO):
            lis.append(k)
        self.x = choice(lis)
        self.y = choice(lis)
        print(lis)
        self.comida.place(x=self.x, y=self.y)

    def keypress(self, event):
        global KEY
        KEY = event.keysym

    def move(self):
        global MX
        global MY
        key = ["Right", "Left", "Up", "Down"]
        com = [MX + PASSO, MX - PASSO, MY - PASSO, MY + PASSO]
        if KEY in key:
            i = key.index(KEY)
            if i < 2:
                MX = com[i]
            else:
                MY = com[i]

    def collision(self):
        global MX
        global MY
        global PONTOS
        if MX < 0 or MX > (self.XX - PASSO):
            return "saiu"

        if MY < 0 or MY > (self.YY - PASSO):
            return "saiu"

        if MX >= (self.x - 8) and MX <= (self.x + 8):
            if MY >= (self.y - 8) and MY <= (self.y + 8):
                PONTOS = PONTOS + 1
                return "comeu"

    def gameover(self):
        self.title = Label(self.table, text="Fim de Jogo",
                           fg="#990000", font=("Arial", 50, "bold"), bg="#4A5B00")
        self.title.place(x=(self.XX // 10), y=(self.YY // 3))

        self.pontos = Label(self.table, text="Pontos: " + str(len(SNAKE) * 5),
                            fg="#ffffff", font=("Arial", 25, "bold"), bg="#4A5B00")
        self.pontos.place(x=(self.XX // 3), y=(self.YY // 3 + 100))

        self.bt = Button(self.table, text="Jogar Novamente",
                         command=self.clear)
        self.bt.place(x=(self.XX // 3 + 20), y=(self.YY // 3 + 150))

    def clear(self):
        global DELAY
        global KEY
        global MX
        global MY
        global SNAKE
        global COORD
        global PASSO
        DELAY = 100
        KEY = "Right"
        MX = 0
        MY = 0
        SNAKE = []
        COORD = []
        PASSO = PASSO
        self.title.destroy()
        self.pontos.destroy()
        self.bt.destroy()
        self.table.destroy()
        self.body()

    def loop(self):
        global SNAKE
        global COORD
        self.move()  # inicia a movimentação
        self.cabeca.place(x=MX, y=MY)  # atualiza a posiçao na tela
        COORD.append((MX, MY))  # armezena a trajetoria em uma lista
        colidiu = self.collision()

        if colidiu == "saiu":  # verifica se saiu do tabuleiro
            self.gameover()
            return

        if colidiu == "comeu":  # verifica se comeu
            self.comida.destroy()
            self.food()
            self.k = Frame(self.table, width=PASSO, height=PASSO, bg="white")
            SNAKE.append(self.k)

        tam = len(SNAKE)  # adiciona 'elos' dinamicamente
        for self.k in SNAKE:
            self.k.place(x=COORD[- tam][0], y=COORD[- tam][1])
            tam = tam - 1

        if len(COORD) > len(SNAKE) + 1:  # limpa a lista de trajetoria
            del(COORD[0])

        cord = COORD[:len(SNAKE)]  # verifica se colidiu consigo mesma
        for x in range(0, len(cord)):
            if MX == cord[x][0] and MY == cord[x][1]:
                self.gameover()
                return

        self.window.after(DELAY, self.loop)  # mantem um looping infinito

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    snake = Game()
    snake.run()
