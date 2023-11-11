import model
import View

def run():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    board_element = " "
    available_moves = {"1a", "2a", "3a", "1b", "2b", "3b", "1c", "2c", "3c"}
    translated_dictionary_of_coordinates = {"1a": 0, "2a": 1, "3a": 2, "1b": 3, "2b": 4, "3b": 5, "1c": 6, "2c": 7,
                                            "3c": 8}
    move = 0
    history_x = set()
    history_o = set()

    while model.init_winner(history_x, history_o) == "dead head":

        if len(available_moves) == 0:
            View.massege("Ходы законччились")
            View.print_board(board)
            View.massege(history_x)
            View.massege(history_o)
            break

        if move % 2 == 0:
            player = "X"
            step = True
        else:
            player = "O"
            step = False

        View.show("Ходит: " , player)
        View.print_board(board)

        while not (board_element in available_moves):
            View.massege("Введите доступную координату:")
            View.massege(available_moves)
            board_element = input()

        available_moves.remove(board_element)
        board[translated_dictionary_of_coordinates.get(board_element)] = player

        if step:
            history_x.add(translated_dictionary_of_coordinates.get(board_element))
        else:
            history_o.add(translated_dictionary_of_coordinates.get(board_element))

        move += 1

    View.show("Победитель: ", model.init_winner(history_x, history_o))
    View.print_board(board)
