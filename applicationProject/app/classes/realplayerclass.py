from mathmodule.mathmodule import choose_2_numbers, choose_from_2_numbers, without_color, is_int

class RealPlayer:
    #TODO: Pole przechowujące plansze gracza, kolor gracza, wybór koloru, wybór dwóch dla kompa itp.
    def __init__(self, d, color, n):
        self.d = d
        self.color = color
        self.n = n

    def check_humanity(self):
        return 1

    def choose(self, which):
        number = input("Wybierz " + which + " liczbę dla komputera: ")
        while not is_int(number):
            number = input("Musisz podać liczbę! Podaj jeszcze raz. ")
        while int(number) > self.n or int(number) < 1 or self.d[int(number)] != 0:
            number = input("Dana liczba nie mieści się w przedziale lub liczba jest już pokolorowana! Podaj inną liczbę. ")
            while not is_int(number):
                number = input("Musisz podać liczbę! Podaj jeszcze raz. ")
        number = int(number)
        return number

    def choose_two(self):
        first_choice = self.choose("pierwszą")
        second_choice = self.choose("drugą")
        while second_choice == first_choice:
            print("Nie możesz wybrać dwóch takich samych liczb!")
            second_choice = self.choose("drugą")
        choose = [first_choice, second_choice]
        return choose

    def color_one(self, first_number, second_number):
        print("Komputer zaproponował Ci liczby", first_number, "i", second_number, ".")
        your_choice = input("Wybierasz: ")
        while not is_int(your_choice):
            your_choice = input("Musisz podać liczbę! Podaj jeszcze raz. ")
        while int(your_choice) != first_number and int(your_choice) != second_number:
            print("Musisz wybrać jedną z powyższych liczb! ")
            your_choice = input("Wybierasz: ")
            while not is_int(your_choice):
                your_choice = input("Musisz podać liczbę! Podaj jeszcze raz. ")
        return int(your_choice)

