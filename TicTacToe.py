from functools import reduce


class TicTacToe:
    def __init__(self):
        self.players = [input("Введите имя первого игрока: "), input("А теперь второго игрока: ")]
        self.turn = 0
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __str__(self):
        res = ""
        for i in range(1, 10):
            j = self.board[i-1]
            if j == 0:
                res += str(i)
            elif j == 1:
                res += "X"
            else:
                res += "O"
            if i % 3 == 0:
                res += "\n"
        return res

    def __repr__(self):
        return str(self)

    def mainloop(self):
        ans = True
        while ans:
            self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.turn = 0
            while True:
                print(self)
                pos = self.make_turn()
                if self.win_move(pos):
                    print(self)
                    print(f"{self.players[self.turn % 2]}, поздравляем!")
                    print(f"Вы не оставили игроку {self.players[(self.turn + 1) % 2]} ни шанса!")
                    break
                if self.turn > 8:
                    print(self)
                    print(f"Уважаемые игроки {self.players[0]} и {self.players[1]}, поле заполнено")
                    print("Это означает, что победила ваша крепкая дружба!")
                    break
            ans = self.ask_for_repetition()

    def make_turn(self):
        pos = input(f"{self.players[self.turn % 2]}, делайте ваш ход: ")
        while not pos.isdigit() or int(pos) not in range(1, 10) or self.board[int(pos)-1] != 0:
            print("Неправильный ход, нужно указать цифру от 1 до 9")
            print("Нельзя также туда ходить, куда ход сделан был")
            pos = input(f"{self.players[self.turn % 2]}, делайте правильный ход: ")
        return int(pos)

    def ask_for_repetition(self):
        print("Уважаеммые игроки, хотите ли вы сыграть ещё одну партию?")
        print("Если да, введите YES, иначе NO")
        i = 0
        inps = ["Если и сейчас не сможете ввести, крестики-нолики слишком сложая игра для вас:",
                "Ну всё, последняя попытка, я не шучу:",
                "Вы думаете, мы тут шутки шутим? Теперь точно последняя попытка:",
                "Ну ладно, даю вам шанс исправиться:"]
        ans = input("Ваш ответ:")
        while ans not in ("YES", "NO"):
            if i == 0:
                print("У вас что, какие-то сложности с напиманием слова 'YES' или 'NO'?")
            elif i == 4:
                print("Хорошо, всё с вами понятно...")
                ans = False
                break
            ans = input(inps[i])
            i += 1
        if ans == "YES":
            return True
        return False

    def win_move(self, pos):
        self.board[pos-1] = self.turn % 2 + 1
        wline = list(filter(lambda x: (x-1) // 3 == (pos-1) // 3, range(pos-2, pos+3)))
        wline = [self.board[i-1] for i in wline]
        wline = reduce(lambda x, y: x*y, wline)
        hline = list(set(range(pos-6, pos+7, 3)).intersection(range(1, 10)))
        hline = [self.board[i-1] for i in hline]
        hline = reduce(lambda x, y: x*y, hline)
        ascline = [1, 5, 9]
        if pos in ascline:
            ascline = [self.board[i-1] for i in ascline]
            ascline = reduce(lambda x, y: x*y, ascline)
        else:
            ascline = 0
        descline = [3, 5, 7]
        if pos in descline:
            descline = [self.board[i-1] for i in descline]
            descline = reduce(lambda x, y: x*y, descline)
        else:
            descline = 0
        target = (self.turn % 2 + 1)**3
        if target in [hline, wline, ascline, descline]:
            return True
        self.turn += 1
        return False


if __name__ == "__main__":
    t = TicTacToe()
    t.mainloop()
    print("Спасибо, что поиграли в эту игру! До встречи!")
