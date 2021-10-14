import unittest
import TicTacToe


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.game = TicTacToe.TicTacToe()
        self.samples_of_strings = ("123\n456\n789\n", "OOO\nOOO\nOOO", "XXX\nXXX\nXXX\n",
                                   "1OX\n4XO\nOXO\n", "123\nXXX\nOOO\n", "12X\nXOX\nOO9\n")
        self.samples_of_boards = ([0,0,0,0,0,0,0,0,0],[2,2,2,2,2,2,2,2,2],[1,1,1,1,1,1,1,1,1],
                                  [0,2,1,0,1,2,2,1,2],[0,0,0,1,1,1,2,2,2],[0,0,1,1,2,1,2,2,0])
        self.samples_of_boards_for_win_move = (([0,0,1,0,0,1,2,2,0],0,9),([0,0,1,0,0,0,1,0,0],0,5),
                                               ([1,2,1,2,0,2,1,2,1],0,5),([1,2,1,2,0,2,1,2,1],1,5),
                                               ([2,2,1,1,1,0,2,2,1],1,6),([0,0,0,0,0,0,0,0,0],0,4))
        self.samples_of_answers_for_win_move = (True, True, True, True, False, False)
        self.samples_of_input_for_turn = ("Введите 9:","Введите 7:","Введите 1:",
                                          "Введите -1, затем 15, а после 'qwerty'. После всего 5:")
        self.samples_of_making_turns = (9, 7, 1, 5)
        self.samples_of_asking_the_rep = ("Введите 'YES':", "Введите 'NO':",
                                          "Введите 'Y', затем 'YE', после 'YES':",
                                          "Введите 5 раз 'What?':")
        self.samples_of_repetition = (True, False, True, False)

    def test_to_string(self):
        for i in range(len(self.samples_of_boards)):
            self.game.board = self.samples_of_boards[i]
            self.assertEqual(str(self.game), self.samples_of_strings[i], msg="Invalid method TicTacToe.__str__()\n")

    def test_move_to_win(self):
        for i in range(len(self.samples_of_boards_for_win_move)):
            self.game.board = self.samples_of_boards_for_win_move[i][0]
            self.game.turn = self.samples_of_boards_for_win_move[i][1]
            move_pos = self.samples_of_boards_for_win_move[i][3]
            ans = self.game.win_move(move_pos)
            self.assertEqual(ans, self.samples_of_answers_for_win_move[i])

    def test_making_a_turn(self):
        i = 0
        for string in self.samples_of_input_for_turn:
            print(string)
            ans = self.game.make_turn()
            self.assertEqual(ans, self.samples_of_making_turns[i])
            i += 1

    def test_ask_the_repetition(self):
        i = 0
        for string in self.samples_of_asking_the_rep:
            print(string)
            ans = self.game.ask_for_repetition()
            self.assertEqual(ans, self.samples_of_repetition[i])
            i += 1

    def tearDown(self) -> None:
        pass
