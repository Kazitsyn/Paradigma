def el_in_set(element, set_c):
    return element in set_c


def init_winner(history_x, history_o):
    winner = ({0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6})

    for el in winner:

        if history_x & el == el:
            return "X"
        elif history_o & el == el:
            return "O"
    else:
        return "dead head"