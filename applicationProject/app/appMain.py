from classes.computerplayerclass import ComputerPlayer, RandomComputerPlayer, EgoisticComputerPlayer, \
    DuelingComputerPlayer
from classes.realplayerclass import RealPlayer
from classes.gameplaymodule import print_game, choose_opponent, game_intro, game_authors_and_title, choose_color, \
    define_computer, set_n, set_k, gameplay, set_computer_color, return_result
import os

#UWAGA, przy odpalaniu w widoku kodu w edytorze (np. PyCharm) możliwe, ze nie skompiluje sie, bo nie znajdzie śćieżki do importów.
#W takim wypadku należy dodać we wszelkich importach app. przed classes
#(wynika to z różnic w czytaniu ścieżki przy eksporcie do EXE, a przy odpalaniu konsoli w edytorze). Poniżej przykład:
#from app.classes.realplayerclass import RealPlayer

game_authors_and_title()
click = int(input("Jeżeli chcesz wyświetlić instrukcję, wpisz 0 i zaakceptuj. Jeżeli nie, zaakceptuj cokolwiek innego."))
if click == 0:
    game_intro()

final = 0
while final == 0:
    n = set_n()
    k = set_k(n)

    d = {}
    for i in range(1, n + 1):
        d[i] = 0

    color = choose_color()
    computer_color = set_computer_color(color)
    opponent = choose_opponent()

    player = RealPlayer(d, color, n)
    computer = ComputerPlayer(d, n, k, computer_color)
    computer = define_computer(opponent, computer_color, n, k, d)

    first_player = player
    second_player = computer
    if color == 2:
        first_player = computer
        second_player = player

    gameplay(d, n, k, first_player, second_player)
    print_game(d)
    final = return_result(n, k, d, first_player, second_player)
    os.system("cls")
