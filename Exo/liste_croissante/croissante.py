def croissance(Liste: list, is_croissant: bool = False):
    if len(Liste) == 1:
        return print(True)
    for i in range(len(Liste) - 1):
        if Liste[i] <= Liste[i + 1]:
            is_croissant = True
        else:
            is_croissant = False
            return print(is_croissant)

    return print(is_croissant)


croissance([20,42,3000, 50])