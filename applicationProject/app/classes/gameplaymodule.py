from classes.computerplayerclass import ComputerPlayer, RandomComputerPlayer, EgoisticComputerPlayer, \
    DuelingComputerPlayer
from mathmodule.mathmodule import series_one_colour, without_color, is_int
from colorama import Fore, Style, init
#Pakiet colorama jest doinstalowany tak, aby exe odpalal sie bez problemu.
#W przypadku, gdy nie chcemy instalowac pakietu colorama wystarczy zakomentowac print_game
#I odkomentowac druga wersje tej funkcji.

def print_game(game):
    init(convert=True, autoreset=True)
    for key, v in game.items():
        if v == 0:
            print(str(key), end=' ')
        elif v == 1:
            print(Fore.BLUE + str(key), end=' ')
        elif v == 2:
            print(Fore.RED + str(key), end=' ')
    print('\n', end='')

'''def print_game(game):
    for key, v in game.items():
        if v == 0:
            print("Liczba " + str(key) + " | Kolor: BRAK")
        elif v == 1:
            print("Liczba " + str(key) + " | Kolor: NIEBIESKI")
        elif v == 2:
            print("Liczba " + str(key) + " | Kolor: CZERWONY")'''

def choose_opponent():
    print("Wybierz swojego przeciwnika. \n"
          "Wpisz 1, jeśli chcesz, by Twój rywal wszelkich wyborów dokonywał losowo. \n"
          "Wpisz 2, jeśli Twoim przeciwnikiem ma być gracz kierujący się wyłącznie swoim własnym dobrem. \n"
          "Wpisz 3, jeśli pragniesz zmierzyć się z kimś, kto nie unika walki.")
    opponent = int(input("Wybierz swojego przeciwnika: "))
    while opponent != 1 and opponent != 2 and opponent != 3:
        opponent = choose_opponent()
    return opponent


def game_intro():
    print("Gra w Wybieranie Szemerediego w tej wersji polega na rozgrywce dwóch graczy (A,B). Każdy z graczy ma przyporządkowany kolor.")
    print("Planszą gry jest zbiór liczb [n], a celem jest utworzenie przez gracza ciagu arytmetycznego długości k w swoim kolorze.")
    print("Gracz A podaje 2 liczby, z których gracz B wybiera jedną, którą koloruje na swój kolor. Następnie następuje zmiana ról.")
    print("Jeżeli nikt z graczy nie stworzy takowego ciągu, to następuje remis.")


def game_authors_and_title():
    print("Gra w Wybieranie Szemerediego - Gracz vs Komputer \n")
    print("Wersja 1.0.0")
    print("Jakub Bezubik, Hubert Grochowski, Tomasz Kapelka")
    print("------------")


def choose_color():
    print("Witaj graczu. Wybierz swój kolor. \n"
          "Wpisz 1, jeśli wolisz niebieski - wtedy to do Ciebie będzie należeć pierwszy ruch. \n"
          "Wpisz 2, jeśli decydujesz się na czerwony - wówczas to komputer rozpocznie rozgrywkę.")
    color = input("A więc wybierasz: ")
    while not is_int(color):
        color = input("Ma być podana liczba! Podaj jeszcze raz. ")
    while int(color) != 1 and int(color) != 2:
        print("To nie jest jedna z oczekiwanych liczb. Wybierz jeszcze raz: ")
        while not is_int(color):
            color = input("Ma być podana liczba! Podaj jeszcze raz. ")
    return int(color)


def define_computer(opponent, computer_color, n, k, d):
    if opponent == 1:
        com = RandomComputerPlayer(d, computer_color, n, k)
    elif opponent == 2:
        com = EgoisticComputerPlayer(d, computer_color, n, k)
    elif opponent == 3:
        com = DuelingComputerPlayer(d, computer_color, n, k)
    return com


def set_n():
    n = input("Ile elementów ma mieć plansza? ")
    while not is_int(n):
        n = input("Ma być liczba! Podaj jeszcze raz. ")
    while int(n) < 3:
        n = input("Za mała długość planszy. Podaj większą liczbę. ")
        while not is_int(n):
            n = input("Ma być liczba! Podaj jeszcze raz. ")
    return int(n)


def set_k(n):
    k = input("Jak długie mają być ciągi? ")
    while not is_int(k):
        k = input("Ma być liczba! Podaj jeszcze raz. ")
    while int(k) < 3 or int(k) > n:
        k = input("Długość ciągu jest zła. Podaj inną długość. ")
        while not is_int(k):
            k = input("Ma być liczba! Podaj jeszcze raz. ")
    return int(k)


def set_computer_color(color):
    if color == 1:
        computer_color = 2
    elif color == 2:
        computer_color = 1
    return computer_color


def gameplay(d, n, k, first_player, second_player):
    while len(without_color(d, n)) > 0:
        print_game(d)
        if len(without_color(d, n)) == 1:
            print("Liczba",without_color(d,n)[0],"została automatycznie pokolorowana na czerwono.")
            d[without_color(d,n)[0]] = 2
            break
        player1_first_choice = first_player.choose_two()
        player2_first_choice = second_player.color_one(player1_first_choice[0], player1_first_choice[1])
        d[player2_first_choice] = second_player.color
        if series_one_colour(n, k, d, second_player.color) == 1:
            break
        print_game(d)
        if len(without_color(d, n)) == 1:
            print("Liczba", without_color(d, n)[0], "została automatycznie pokolorowana na niebiesko.")
            d[without_color(d, n)[0]] = 1
            break
        player2_second_choice = second_player.choose_two()
        player1_second_choice = first_player.color_one(player2_second_choice[0], player2_second_choice[1])
        d[player1_second_choice] = first_player.color
        if series_one_colour(n, k, d, first_player.color) == 1:
            break


def return_result(n, k, d, first_player, second_player):
    if series_one_colour(n, k, d, first_player.color) == 1:
        if first_player.check_humanity() == 1:
            print("Brawo! Tryumf człowieka nad maszyną!")
            final = int(input("Naciśnij 0 i zaakceptuj, aby zagrać znowu. Aby skończyć rozgrywkę, zaakceptuj cokolwiek innego. "))
            return final
        else:
            print("Niestety, komputer Cię pokonał :(")
            final = int(input("Naciśnij 0 i zaakceptuj, aby zagrać znowu. Aby skończyć rozgrywkę, zaakceptuj cokolwiek innego. "))
            return final

    if series_one_colour(n, k, d, second_player.color) == 1:
        if second_player.check_humanity() == 1:
            print("Brawo! Tryumf człowieka nad maszyną!")
            final = int(input("Naciśnij 0 i zaakceptuj, aby zagrać znowu. Aby skończyć rozgrywkę, zaakceptuj cokolwiek innego. "))
            return final
        else:
            print("Niestety, komputer Cię pokonał :(")
            final = int(input("Naciśnij 0 i zaakceptuj, aby zagrać znowu. Aby skończyć rozgrywkę, zaakceptuj cokolwiek innego. "))
            return final

    if series_one_colour(n, k, d, first_player.color) == 0 and series_one_colour(n, k, d, second_player.color) == 0:
        print("Nikomu nie udało się wygrać :( Spróbuj jeszcze raz!")
        final = int(input("Naciśnij 0 i zaakceptuj, aby zagrać znowu. Aby skończyć rozgrywkę, zaakceptuj cokolwiek innego. "))
        return final
