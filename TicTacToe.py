class ttt:
    def __init__(self):
        self.board = []
    def c_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)
    def s_board(self):
        for i in self.board:
            for j in i:
                print(j,end="")
            print()
    def player(self):
        return True
    def player_change(self,player1):
        if player1 == "X":
            return True
        else:
            return False

    def mark(self,row,clm,player):
        try:
            self.board[row][clm] = player
        except:
            print("geçersiz sayı")

    def win_check(self,player):
        win = None
        n = len(self.board)
        #y#
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
        #d#
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
        #ç#
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win

    def Draw_check(self):
        for i in self.board:
            for j in i:
                if j == "-":
                    return False
        return True

    def start(self):
            self.c_board()
            if self.player() == True:
                player1 = "X"
            else:
                player1 = "O"

            while True:
                print("Player {} Turn".format(player1))

                self.s_board()

                try:
                    row, clm = list(
                        map(int, input("Mark:").split()))
                    print()
                except:
                    print("geçersiz sayı")
                    continue

                self.mark(row - 1, clm - 1, player1)

                if self.Draw_check() == True:
                    print("Draw")
                    break

                if self.win_check(player1):
                    self.s_board()
                    print("Player {} wins".format(player1))
                    break

                if self.player_change(player1):
                    player1 = "O"
                else:
                    player1 = "X"

q = ttt()
q.start()
