from classes.computerplayerclass import ComputerPlayer, RandomComputerPlayer, EgoisticComputerPlayer, \
    DuelingComputerPlayer
from classes.realplayerclass import RealPlayer
#from app.classes.gameplayclass import Gameplay
from mathmodule.mathmodule import series_one_colour, without_color

print("Gra w Wybieranie Szemerediego - Gracz vs Komputer \n")
print("Wersja BETA Aplikacji - 3.05")
print("Jakub Bezubik, Hubert Grochowski, Tomasz Kapelka")
print("Do dodania instrukcja, mozliwosc zapetlania rozgrywki, sformatowanie wygladu rozgrywki")
print("Do poprawienia ewentualne bledy w kodzie, ktore wyjda w trakcie testow do koncowej wersji aplikacji oraz ulozenie kodu")
print("------------")
n = int(input("Ile elementów ma mieć plansza? "))
k = int(input("Jak długie mają być ciągi? "))
# Game = Gameplay(n, k)

dict = {}
for i in range(1, n + 1):
    dict[i] = 0

print("Witaj graczu. Wybierz swój kolor. \n"
      "Wpisz 1, jeśli wolisz niebieski - wtedy to do Ciebie będzie należeć pierwszy ruch. \n"
      "Wpisz 2, jeśli decydujesz się na czerwony - wówczas to komputer rozpocznie rozgrywkę.")
color = int(input("A więc wybierasz: "))
while color != 1 and color != 2:
    print("To nie jest jedna z oczekiwanych liczb. Wybierz jeszcze raz: ")
    color = int(input("A więc wybierasz: "))
computer_color = 0
if color == 1:
    computer_color = 2
elif color == 2:
    computer_color = 1
print("Wybierz swojego przeciwnika. \n"
      "Wpisz 1, jeśli chcesz, by Twój rywal wszelkich wyborów dokonywał losowo. \n"
      "Wpisz 2, jeśli Twoim przeciwnikiem ma być gracz kierujący się wyłącznie swoim własnym dobrem. \n"
      "Wpisz 3, jeśli pragniesz zmierzyć się z kimś, kto nie unika walki.")
opponent = int(input("Wybierz swojego przeciwnika: "))
while opponent!=1 and opponent!=2 and opponent!=3:
    print("Podales blednie rodzaj przeciwnika.\n"
          "Wpisz 1, jeśli chcesz, by Twój rywal wszelkich wyborów dokonywał losowo. \n"
          "Wpisz 2, jeśli Twoim przeciwnikiem ma być gracz kierujący się wyłącznie swoim własnym dobrem. \n"
          "Wpisz 3, jeśli pragniesz zmierzyć się z kimś, kto nie unika walki.")
    opponent = int(input("Wybierz swojego przeciwnika: "))
Player = RealPlayer(dict, color, n)
Computer = ComputerPlayer(dict, n, k, computer_color)
if opponent == 1:
    Computer = RandomComputerPlayer(dict, computer_color, n, k)
elif opponent == 2:
    Computer = EgoisticComputerPlayer(dict, computer_color, n, k)
elif opponent == 3:
    Computer = DuelingComputerPlayer(dict, computer_color, n, k)

FirstPlayer = Player
SecondPlayer = Computer
if color == 2:
    FirstPlayer = Computer
    SecondPlayer = Player

while len(without_color(dict, n)) > 0:
    for k, v in dict.items():
        if v==0:
            print("Liczba: "+ str(k) +" Kolor: ")
        elif v==1:
            print("Liczba: "+ str(k) +" Kolor: Niebieski")
        elif v==2:
            print("Liczba: "+ str(k) +" Kolor: Czerwony")
    if len(without_color(dict, n)) == 1:
        print("Liczba",without_color(dict,n)[0],"została automatycznie pokolorowana na czerwono.")
        dict[without_color(dict,n)[0]] = 2
        break
    player1_first_choice = FirstPlayer.choose_two()
    player2_first_choice = SecondPlayer.color_one(player1_first_choice[0], player1_first_choice[1])
    dict[player2_first_choice] = SecondPlayer.color
    if series_one_colour(n, k, dict, SecondPlayer.color) == 1:
        break
    for k, v in dict.items():
        if v == 0:
            print("Liczba: " + str(k) + " Kolor: ")
        elif v == 1:
            print("Liczba: " + str(k) + " Kolor: Niebieski")
        elif v == 2:
            print("Liczba: " + str(k) + " Kolor: Czerwony")
    if len(without_color(dict, n)) == 1:
        print("Liczba", without_color(dict, n)[0], "została automatycznie pokolorowana na niebiesko.")
        dict[without_color(dict, n)[0]] = 1
        break
    player2_second_choice = SecondPlayer.choose_two()
    player1_second_choice = FirstPlayer.color_one(player2_second_choice[0], player2_second_choice[1])
    dict[player1_second_choice] = FirstPlayer.color
    if series_one_colour(n, k, dict, FirstPlayer.color) == 1:
        break

for k, v in dict.items():
    if v == 0:
        print("Liczba: " + str(k) + " Kolor: ")
    elif v == 1:
        print("Liczba: " + str(k) + " Kolor: Niebieski")
    elif v == 2:
        print("Liczba: " + str(k) + " Kolor: Czerwony")

if series_one_colour(n, k, dict, FirstPlayer.color) == 1:
    if FirstPlayer.check_humanity() == 1:
        print("Brawo! Tryumf człowieka nad maszyną!")
        final = input("Naciśnij cokolwiek, aby zakończyć rozgrywkę.")
    else:
        print("Niestety, komputer Cię pokonał :(")
        final = input("Naciśnij cokolwiek, aby zakończyć rozgrywkę.")

if series_one_colour(n, k, dict, SecondPlayer.color) == 1:
    if SecondPlayer.check_humanity() == 1:
        print("Brawo! Tryumf człowieka nad maszyną!")
        final = input("Naciśnij cokolwiek, aby zakończyć rozgrywkę.")
    else:
        print("Niestety, komputer Cię pokonał :(")
        final = input("Naciśnij cokolwiek, aby zakończyć rozgrywkę.")

if series_one_colour(n, k, dict, FirstPlayer.color) == 0 and series_one_colour(n, k, dict, SecondPlayer.color) == 0:
    print("Nikomu nie udało się wygrać :( Spróbuj jeszcze raz!")
    final = input("Naciśnij cokolwiek, aby zakończyć rozgrywkę.")
