from mathmodule.mathmodule import without_color, choose_from_2_numbers, choose_2_numbers
from classes.realplayerclass import RealPlayer
import random

class ComputerPlayer:
    #TODO Pole przechowujące plansze kompa, kolor kompa, "nazwę" kompa, polimorfizmy do klas dziedziczących
    def __init__(self, d, color, n, k):
        self.d = d
        self.color = color
        self.n = n
        self.k = k

    def choose_two(self):
        pass

    def color_one(self, first_number, second_number):
        pass

    def real_players_color(self):
        I=[1,2]
        del I[self.color - 1]
        return I[0]

    def check_humanity(self):
        return 0

class RandomComputerPlayer(ComputerPlayer):
    #TODO Implementacja wyboru par, kolorowania itp. w strategii losowej
    def choose_two(self):
        return random.sample(without_color(self.d, self.n), 2)

    def color_one(self, first_number, second_number):
        list = [first_number, second_number]
        return random.choice(list)


class EgoisticComputerPlayer(ComputerPlayer):
    # TODO Implementacja wyboru par, kolorowania itp. w strategii egoistycznej
    def choose_two(self):
        return choose_2_numbers(self.n, self.k, self.d, EgoisticComputerPlayer.real_players_color(self), self.color)

    def color_one(self, first_number, second_number):
        return choose_from_2_numbers(self.n, self.k, self.d, self.color, first_number, second_number)


class DuelingComputerPlayer(ComputerPlayer):
    # TODO Implementacja wyboru par, kolorowania itp. w strategii atakującej
    def choose_two(self):
        return choose_2_numbers(self.n, self.k, self.d, DuelingComputerPlayer.real_players_color(self), DuelingComputerPlayer.real_players_color(self))

    def color_one(self, first_number, second_number):
        return choose_from_2_numbers(self.n, self.k, self.d, DuelingComputerPlayer.real_players_color(self), first_number, second_number)