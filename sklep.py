import random
class reader:
    def __init__(self):
        self.file = None
        self.lines = []
        self.prices = []  # Rename attribute

    

    def open_file(self, filename):
        self.file = open(filename, 'r', encoding='utf-8')

    def read_lines(self):
        self.file.seek(0)  # Reset file pointer to the beginning
        linie = self.file.readlines()
        for i in range(len(linie)):
            if linie[i].strip():  # Check if the line is not empty
                self.lines.append(linie[i].strip())
        return self.lines
    def ceny(self):  # Keep method name
        for line in self.lines:
            if len(self.lines) >= 2:
                try:
                    cena = random.randint(random.randint(1, 49), random.randint(50, 100))
                    self.prices.append(cena)  # Use new name
                except ValueError:
                    pass
        return self.prices
    def produkt_cena(self):
        produkty_ceny = {}
        for i in range(len(self.lines)):
            if i < len(self.prices):
                produkty_ceny[self.lines[i]] = self.prices[i]
        return produkty_ceny
    def sort_alphabetically_dictionary(self):
        sorted_dict = dict(sorted(self.produkt_cena().items()))
        return sorted_dict
    def sort_by_price_dictionary(self):
        sorted_dict = dict(sorted(self.produkt_cena().items(), key=lambda item: item[1]))
        return sorted_dict
    
    def dopisuj_do_pliku(self, filename, text):
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(text.lower() + '\n')


    def close_file(self):
        if self.file:
            self.file.close()
            self.file = None 


object = reader()
object.open_file('lista.txt')
print(object.read_lines())
object.ceny()
print(f"po kolei jak podano: \n {object.produkt_cena()}")
print(f"posortowane alfabetycznie: \n {object.sort_alphabetically_dictionary()}")
print(f"posortowane po cenie: \n {object.sort_by_price_dictionary()}")
zapytanie = input("Czy chcesz dopisać coś do pliku? (tak/nie): ")
if zapytanie.lower() == 'tak':
    ile = int(input("Ile tekstów chcesz dopisać? "))
    for a in range(ile):   
        tekst = input("Wpisz tekst do dopisania: ")
        object.dopisuj_do_pliku('lista.txt', tekst)
else :
    print("Nie dopisano nic do pliku.")
object.close_file()
if object.file is None:
    print(f"Plik został zamknięty. \n Dziękuję za skorzystanie z programu.")


