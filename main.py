def cel_for_far(temp_in_cel):
    temp_in_far = (9 * temp_in_cel + (32*5))/5
    return round(temp_in_far, 2)


def far_for_cel(temp_in_far):
    temp_in_cel = (5 * (temp_in_far - 32))/9
    return round(temp_in_cel, 2)


unit_selection = input('''Podaj jednostkę temperatury którą chcesz zamienić: \nC - Celsjusz \nF - Farenhait \n''')


if unit_selection.upper() == 'C':
    value_cel = float(input('''Podaj wartośc w Celsjuszach którą chcesz przekonwertować: '''))
    print(str(value_cel) + f" stopni Celsjusza wynosi {cel_for_far(value_cel)} stopni Farenhaita")
elif unit_selection.upper() == 'F':
    value_far = float(input('''Podaj wartośc w Farenhaitach którą chcesz przekonwertować: '''))
    print(str(value_far) + f" stopni Farenhaita  wynosi {far_for_cel(value_far)} stopni Celsjusza")
else:
    print(''''Nie podano prawidłowej wartości \nNależy podać C lub F!!''')
