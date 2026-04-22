#zadanie 1
class FileProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.lines = []

    def open_file(self):
        self.file = open(self.filename, 'r', encoding='utf-8')

    def read_lines(self):
        self.lines = self.file.readlines()

    def even_lines(self):
        return [line.strip() for i, line in enumerate(self.lines) if i % 2 == 1]

    def duplicated_words(self):
        words = []
        for line in self.lines:
            words.extend(line.strip().split())

        duplicates = set([w for w in words if words.count(w) > 1])
        return duplicates

    def count_vowels(self, word):
        vowels = "aeiouyąęóAEIOUYĄĘÓ"
        return sum(1 for c in word if c in vowels)

    def word_with_most_vowels(self):
        duplicates = self.duplicated_words()
        return max(duplicates, key=self.count_vowels, default=None)

    def close_file(self):
        if self.file:
            self.file.close()


# TEST
fp = FileProcessor("test.txt")
fp.open_file()
fp.read_lines()

print("Even lines:", fp.even_lines())
print("Duplicates:", fp.duplicated_words())
print("Best word:", fp.word_with_most_vowels())

fp.close_file()
#zadanie 2
import random
from collections import Counter

class Lotto:
    def __init__(self, numbers):
        if len(numbers) != 6:
            raise ValueError("Must have 6 numbers")
        self.numbers = sorted(numbers)

    def sprawdz(self, other):
        return sorted(self.numbers) == sorted(other.numbers)

    @staticmethod
    def generate_set():
        return sorted(random.sample(range(49), 6))


def simulate_lotto():
    results = []
    for _ in range(1000):
        draw = tuple(Lotto.generate_set())
        results.append(draw)

    counter = Counter(results)
    sorted_results = counter.most_common()

    filename = f"{sorted_results[0][0][0]}_{sorted_results[0][0][1]}.txt"
    with open(filename, "w") as f:
        for combo, count in sorted_results:
            f.write(f"{combo} -> {count}\n")

    return sorted_results


# TEST
l1 = Lotto([1,2,3,4,5,6])
l2 = Lotto([6,5,4,3,2,1])
print(l1.sprawdz(l2))

simulate_lotto()
#ZADANIE 3
class Czytelnik:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.lines = []

    def otworz(self):
        self.file = open(self.filename, 'r', encoding='utf-8')

    def czytam(self):
        self.lines = [line.strip() for i, line in enumerate(self.file) if i % 2 == 0]

    def szukam(self, text):
        return any(text in line for line in self.lines)

    def licz(self, char):
        return sum(line.count(char) for line in self.lines)

    def najczestsza_litera(self):
        from collections import Counter
        all_text = "".join(self.lines)
        counter = Counter(all_text)
        return counter.most_common(1)[0]

    def zamykam(self):
        self.file.close()


# TEST
cz = Czytelnik("test.txt")
cz.otworz()
cz.czytam()
print(cz.szukam("test"))
print(cz.licz("a"))
print(cz.najczestsza_litera())
cz.zamykam()
#zadanie 4
import random
import statistics

class Stats:
    def __init__(self):
        self.data = [random.randint(0, 100) for _ in range(500)]

    def minimalny(self):
        return min(self.data)

    def maksymalny(self):
        return max(self.data)

    def sumuje(self):
        return sum(self.data)

    def odchyl(self):
        return statistics.stdev(self.data)

    def moda(self):
        return statistics.mode(self.data)

    def mediana(self):
        return statistics.median(self.data)

    def zapisuje(self):
        filename = f"{self.data[0]}.txt"
        with open(filename, "w") as f:
            f.write("Data:\n")
            f.write(str(self.data) + "\n")
            f.write(f"Min: {self.minimalny()}\n")
            f.write(f"Max: {self.maksymalny()}\n")
            f.write(f"Sum: {self.sumuje()}\n")
            f.write(f"Std: {self.odchyl()}\n")
            f.write(f"Mode: {self.moda()}\n")
            f.write(f"Median: {self.mediana()}\n")


# TEST
s = Stats()
s.zapisuje()


#ZADANIE 5
class Liczba:
    def __init__(self, value):
        self.value = int(value)


class Wyraz:
    def __init__(self, text):
        self.text = str(text)


def dodaj(a, b):
    if isinstance(a, Liczba) and isinstance(b, Liczba):
        return a.value + b.value

    if isinstance(a, Wyraz) and isinstance(b, Wyraz):
        return a.text + b.text

    if isinstance(a, Wyraz) and isinstance(b, Liczba):
        return b.value + ord(a.text[-1])

    if isinstance(a, Liczba) and isinstance(b, Wyraz):
        return a.value + ord(b.text[-1])


def odejmij(a, b):
    if isinstance(a, Liczba) and isinstance(b, Liczba):
        return a.value - b.value

    if isinstance(a, Wyraz) and isinstance(b, Wyraz):
        return a.text if len(a.text) > len(b.text) else b.text

    if isinstance(a, Wyraz) and isinstance(b, Liczba):
        return "Nie mozna odjac stringa i liczby"


def zapisz(filename, add_result, sub_result):
    with open(filename, "w") as f:
        f.write(f"Dodaj: {add_result}\n")
        f.write(f"Odejmij: {sub_result}\n")


# TEST
a = Liczba(10)
b = Liczba(5)
w1 = Wyraz("kot")
w2 = Wyraz("pies")

add_res = dodaj(w1, a)
sub_res = odejmij(w1, w2)

zapisz("wynik.txt", add_res, sub_res)