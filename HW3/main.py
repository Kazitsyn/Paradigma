import Controller

Controller.run()

# def print_board(n):
#     print("  a  b  c ")
#     print("1[" + n[0] + "][" + n[3] + "][" + n[6] + "]")
#     print("2[" + n[1] + "][" + n[4] + "][" + n[7] + "]")
#     print("3[" + n[2] + "][" + n[5] + "][" + n[8] + "]")
#
#
# def el_in_set(element, set_c):
#     return element in set_c
#
#
# def init_winner(history_x, history_o):
#     winner = ({0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6})
#
#     for el in winner:
#
#         if history_x & el == el:
#             return "X"
#         elif history_o & el == el:
#             return "O"
#     else:
#         return "dead head"
#
#
# board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
# board_element = " "
# available_moves = {"1a", "2a", "3a", "1b", "2b", "3b", "1c", "2c", "3c"}
# translated_dictionary_of_coordinates = {"1a": 0, "2a": 1, "3a": 2, "1b": 3, "2b": 4, "3b": 5, "1c": 6, "2c": 7, "3c": 8}
# move = 0
# history_x = set()
# history_o = set()
#
# while init_winner(history_x, history_o) == "dead head":
#
#     if len(available_moves) == 0:
#         print("Ходы законччились")
#         print_board(board)
#         print(history_x)
#         print(history_o)
#         break
#
#     if move % 2 == 0:
#         player = "X"
#         step = True
#     else:
#         player = "O"
#         step = False
#
#     print("Ходит: " + player)
#     print_board(board)
#
#     while not el_in_set(board_element, available_moves):
#         print("Введите доступную координату:")
#         print(available_moves)
#         board_element = input()
#
#     available_moves.remove(board_element)
#     board[translated_dictionary_of_coordinates.get(board_element)] = player
#
#     if step:
#         history_x.add(translated_dictionary_of_coordinates.get(board_element))
#     else:
#         history_o.add(translated_dictionary_of_coordinates.get(board_element))
#
#     move += 1
#
#
# print("Победитель: ", init_winner(history_x, history_o))