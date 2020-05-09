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

    def status(self):
        x_count, o_count = 0, 0
        x_row = [0 for _i in range(8)]
        o_row = [0 for _i in range(8)]
        for r in range(len(self.field)):
            for c in range(len(self.field[r])):
                if self.field[r][c] == "X":
                    x_count += 1
                elif self.field[r][c] == "O":
                    o_count += 1
                self.add_to_row(c, o_row, r, x_row, r)
                self.add_to_row(r, o_row, c, x_row, r + 3)
                if r == c and not (r == 0 and c == 2 or r == 2 and c == 0):
                    self.add_to_row(c, o_row, r, x_row, 6)
        self.add_to_row(0, o_row, 2, x_row, 7)
        self.add_to_row(1, o_row, 1, x_row, 7)
        self.add_to_row(2, o_row, 0, x_row, 7)
        x_row.sort()
        o_row.sort()
        if abs(x_count - o_count) > 1 or (x_row[-1] == 3 and o_row[-1] == 3):
            print("Impossible")
        elif x_row[-1] == 3:
            print("X wins")
        elif o_row[-1] == 3:
            print("O wins")
        elif x_count + o_count < 9:
            print("Game not finished")
        else:
            print("Draw")

    def add_to_row(self, c, o_row, r, x_row, pos):
        if self.field[r][c] == "X":
            x_row[pos] += 1
        elif self.field[r][c] == "O":
            o_row[pos] += 1

    def process_coords(self):
        coords = input("Enter the coordinates")
        coords = coords.split()
        if len(coords) != 2:
            print("You should enter exactly 2 digits!")
            return False
        if not coords[0].isdigit() or not coords[1].isdigit():
            print("You should enter numbers!")
            return False
        coords = [int(c) for c in coords]
        if not 1 <= coords[0] <= 3 or not 1 <= coords[1] <= 3:
            print("Coordinates should be from 1 to 3!")
            return False
        if self.field[3 - coords[1]][coords[0] - 1] != "_":
            print("This cell is occupied! Choose another one!")
            return False
        self.field[3 - coords[1]][coords[0] - 1] = "X"
        return True


game = TicTacToe()
game.read_field_state(input("Enter cells"))
game.print_field()
success = game.process_coords()
while not success:
    success = game.process_coords()
game.print_field()

