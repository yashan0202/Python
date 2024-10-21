class DotConnectGame:
    def __init__(self, size):
        self.size = size  # size of the grid (n x n)
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.lines = set()  # to store connected lines (edges)
        self.boxes = [[None for _ in range(size - 1)] for _ in range(size - 1)]  # stores owner of the box
        self.players = ['Player 1', 'Player 2']
        self.current_player = 0

    def print_board(self):
        print("Current Board:")
        for i in range(self.size):
            for j in range(self.size):
                if j < self.size - 1:
                    if (i, j, i, j + 1) in self.lines:
                        print('•──', end='')  # horizontal line
                    else:
                        print('•   ', end='')  # empty space between dots
            print('•')
            if i < self.size - 1:
                for j in range(self.size):
                    if (i, j, i + 1, j) in self.lines:
                        print('│   ', end='')  # vertical line
                    else:
                        print('    ', end='')  # empty space below dots
                print()

    def is_valid_move(self, r1, c1, r2, c2):
        if r1 == r2 and abs(c1 - c2) == 1 or c1 == c2 and abs(r1 - r2) == 1:
            return True
        return False

    def add_line(self, r1, c1, r2, c2):
        if self.is_valid_move(r1, c1, r2, c2) and (r1, c1, r2, c2) not in self.lines:
            self.lines.add((r1, c1, r2, c2))
            self.lines.add((r2, c2, r1, c1))  # add reverse direction for bidirectional connection
            return True
        return False

    def check_for_boxes(self, r1, c1, r2, c2):
        # Check if this move completes any boxes
        points = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            r, c = (r1 + r2) // 2 + dr, (c1 + c2) // 2 + dc
            if 0 <= r < self.size - 1 and 0 <= c < self.size - 1:
                if all([(r, c, r + 1, c) in self.lines,
                        (r, c, r, c + 1) in self.lines,
                        (r + 1, c, r + 1, c + 1) in self.lines,
                        (r, c + 1, r + 1, c + 1) in self.lines]):
                    if not self.boxes[r][c]:
                        self.boxes[r][c] = self.players[self.current_player]
                        points += 1
        return points

    def is_full(self):
        return all(all(row) for row in self.boxes)

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def play(self):
        print(f"Welcome to the Dot Connect Game ({self.size}x{self.size} grid)!")
        while not self.is_full():
            self.print_board()
            print(f"{self.players[self.current_player]}'s turn:")
            try:
                r1, c1 = map(int, input("Enter coordinates of the first dot (row col): ").split())
                r2, c2 = map(int, input("Enter coordinates of the second dot (row col): ").split())
            except ValueError:
                print("Invalid input, please enter valid coordinates.")
                continue

            if not (0 <= r1 < self.size and 0 <= r2 < self.size and 0 <= c1 < self.size and 0 <= c2 < self.size):
                print("Invalid coordinates. Please try again.")
                continue

            if self.add_line(r1, c1, r2, c2):
                points_scored = self.check_for_boxes(r1, c1, r2, c2)
                if points_scored > 0:
                    print(f"{self.players[self.current_player]} completed {points_scored} box(es)!")
                else:
                    self.switch_player()
            else:
                print("Invalid move. Please try again.")

        # Game over: declare winner
        p1_boxes = sum(row.count(self.players[0]) for row in self.boxes)
        p2_boxes = sum(row.count(self.players[1]) for row in self.boxes)

        print("Game over!")
        print(f"{self.players[0]} completed {p1_boxes} boxes.")
        print(f"{self.players[1]} completed {p2_boxes} boxes.")

        if p1_boxes > p2_boxes:
            print(f"{self.players[0]} wins!")
        elif p2_boxes > p1_boxes:
            print(f"{self.players[1]} wins!")
        else:
            print("It's a tie!")

# Play a 3x3 grid game
game = DotConnectGame(3)
game.play()
