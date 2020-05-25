from mathmodule.mathmodule import choose_2_numbers, choose_from_2_numbers, without_color

class RealPlayer:
    #TODO: Pole przechowujące plansze gracza, kolor gracza, wybór koloru, wybór dwóch dla kompa itp.
    def __init__(self, d, color, n):
        self.d = d
        self.color = color
        self.n = n

    def check_humanity(self):
        return 1

    def choose_two(self):
        first_choice = int(input("Wybierz pierwszą liczbę dla komputera: "))
        while first_choice > self.n or first_choice < 1:
            first_choice = int(input("Dana liczba nie mieści się w przedziale! Podaj inną liczbę. "))
        while self.d[first_choice] != 0:
            print("Ta liczba jest już pokolorowana!")
            first_choice = int(input("Wybierz pierwszą liczbę dla komputera: "))
        second_choice = int(input("Wybierz drugą liczbę dla komputera: "))
        while second_choice > self.n or second_choice < 1:
            second_choice = int(input("Dana liczba nie mieści się w przedziale! Podaj inną liczbę. "))
        while self.d[second_choice] != 0:
            print("Ta liczba jest już pokolorowana!")
            second_choice = int(input("Wybierz drugą liczbę dla komputera: "))
        while second_choice == first_choice:
            print("Nie możesz wybrać dwóch takich samych liczb!")
            second_choice = int(input("Wybierz drugą liczbę dla komputera: "))
        choose = [first_choice, second_choice]
        return choose

    def color_one(self, first_number, second_number):
        print("Komputer zaproponował Ci liczby", first_number, "i", second_number, ".")
        your_choice = int(input("Wybierasz: "))
        while your_choice != first_number and your_choice != second_number:
           print ("Musisz wybrać jedną z powyższych liczb! ")
           your_choice = int(input("Wybierasz: "))
        return your_choice

