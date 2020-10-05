# Name: Senhe Hao
# Assignment: Lab 6 Part 3
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    # Initializes the chess board
    chess_board = [
        ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["r", "n", "b", "q", "k", "b", "n", "r"],
    ]
    # The loop that lets this whole thing run
    while True:
        # Prints the board
        for i in chess_board:
            print(i)
        # Reads in the input
        print("Input the position of the piece ane where you want to put it.")
        pos_1 = int(input("Input how far down the piece is. From 1-8"))
        pos_2 = int(input("Input how far right the piece is. From 1-8"))
        # Verifies input
        try:
            if chess_board[pos_1 - 1][pos_2 - 1] == ".":
                print("Error, there is no piece in this area")
                exit()
        except IndexError:
            print("This is an invalid move. The position is not on the board.")
            continue
        # Another input
        end_1 = int(input("Input how far down you want to move it. From 1-8"))
        end_2 = int(input("Input how far right you want to move it. From 1-8"))
        # Tries to move, if you can't then it's an invalid move.
        try:
            chess_board[end_1-1][end_2-1] = chess_board[pos_1-1][pos_2-1]
            chess_board[pos_1-1][pos_2-1] = "."
        except IndexError:
            print("This is an invalid move. The position is not on the board.")


# If file is run call main
if __name__ == "__main__":
    main()
