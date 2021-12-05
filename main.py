from board import Board


def main():
    counter = 0
    finished = False
    board = Board()
    while counter < 21 and not finished:
        color = input(f"Please enter a color to the game. you have {21 - counter} moves left.")
        finished = board.move(color)
        counter += 1
    return f"You {'Win!!!' if finished else 'Lose'}"


if __name__ == '__main__':
    result = main()
    print(result)
