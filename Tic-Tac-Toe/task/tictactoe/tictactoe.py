# write your code here
class TicTacToe:
    def __init__(self):
        self.field = [["_" for _i in range(3)] for _i in range(3)]

    def print_field(self):
        print("---------")
        for row in self.field:
            print(f"| {' '.join(row)} |")
        print("---------")

    def read_field_state(self, state):
        for i in range(len(state)):
            self.field[i // 3][i % 3] = state[i]


game = TicTacToe()
game.read_field_state(input())
game.print_field()
