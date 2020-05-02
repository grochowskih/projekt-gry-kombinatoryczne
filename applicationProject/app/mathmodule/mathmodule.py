#TODO Funkcje odpowiadające za obliczenia matematyczne
import random

def create_all_series(n, k):
    series = [[a+n*r for n in range(k)] for a in range(1, n+1, 1) for r in range(1, int((n-1)/(k-1))+1, 1)]
    series_copy = series.copy()
    for ser in series_copy:
        for el in ser:
            if el > n:
                series.remove(ser)
                break
    return series

def series_include_element(el, series):
    result = [ser for ser in series if el in ser]
    return result

def without_color(dict, n):
    list = []
    for i in range(1, n+1):
        if dict[i] == 0:
            list.append(i)
    return list

def values_of_points(n, k, dict, players_color):
    lista = without_color(dict, n)
    list = {}
    for el1 in lista:
        series = series_include_element(el1, create_all_series(n, k))
        value = 0
        for el2 in series:
            for el3 in el2:
                if dict[el3] == players_color:
                    value = value + 1
        list[el1] = value
    return list

def series_one_colour(n, k, dict, players_color):
    for el in dict:
        for el1 in series_include_element(el, create_all_series(n, k)):
            if all(dict[el2] == players_color for el2 in el1):
                return 1
    return 0

def choose_2_numbers(n, k, dict, players_color):
    lista = values_of_points(n, k, dict, players_color)
    # print(lista)
    if len(lista) < 2:
        print('Została tylko jedna liczba')
        number = random.choice(list(lista))
        return number
    lista_copy = lista.copy()
    for el in lista:
        dict[el] = players_color
        if series_one_colour(n, k, dict, players_color) == 1:
            del lista_copy[el]
        dict[el] = 0
    if len(lista_copy) == 0:
        first_number = random.choice(list(lista))
        del lista[first_number]
        second_number = random.choice(list(lista))
        choose = [first_number, second_number]
        return choose
    elif len(lista_copy) == 1:
        first_number = random.choice(list(lista_copy))
        del lista[first_number]
        second_number = random.choice(list(lista))
        choose = [first_number, second_number]
        return choose
    else:
        temp = min(lista_copy.values())
        res = [key for key in lista_copy if lista_copy[key] == temp]
        first_number = random.choice(res)
        res.remove(first_number)
        if len(res) == 0:
            del lista_copy[first_number]
            temp = min(lista_copy.values())
            res = [key for key in lista_copy if lista_copy[key] == temp]
            second_number = random.choice(res)
            choose = [first_number, second_number]
            return choose
        second_number = random.choice(res)
        choose = [first_number, second_number]
        return choose

def choose_from_2_numbers(n, k, dict, players_color, first_number, second_number):
    series1 = series_include_element(first_number, create_all_series(n, k))
    series2 = series_include_element(second_number, create_all_series(n, k))
    value1 = 0
    for el in series1:
        for el1 in el:
            if dict[el1] == players_color:
                value1 = value1 + 1
    value2 = 0
    for el in series2:
        for el1 in el:
            if dict[el1] == players_color:
                value2 = value2 + 1
    if value1 > value2:
        return first_number
    else:
        return second_number



