# write your code here
import random
field = [[None for i in range(3)] for i in range(3)]
options = ("X", "O")
field[0][0] = random.choice(options)
field[1][0] = random.choice(options)
field[2][0] = random.choice(options)
field[0][1] = random.choice(options)
field[1][1] = random.choice(options)
field[2][1] = random.choice(options)
field[0][2] = random.choice(options)
field[1][2] = random.choice(options)
field[2][2] = random.choice(options)
for row in field:
    print(" ".join(row))
