import random
import string
class shopkeeper:
    def __init__(self):
        self.name =None #puste na start
        self.age = None
        self.sylable = ['ka', 'lo', 'mi', 'ra', 'ta', 'ze', 'na', 'su', 'vi', 'do']
        self.style = ['casual', 'formal', 'sporty', 'elegant', 'vintage']
        self.mood = ['happy', 'sad', 'angry', 'excited', 'bored']
    def generate_data(self):
        name = ""
        folder = {}
        for i in range(2):
            name += random.choice(self.sylable)
        self.name = name
        self.age = random.randint(20, 60)
        # Użyj innych nazw zmiennych
        self.wybrany_style = random.choice(self.style)
        self.wybrany_mood = random.choice(self.mood)
        folder[self.name] = {
            "age": self.age,
            "style": self.wybrany_style,
            "mood": self.wybrany_mood
        }
        return folder
    def dopisz_do_pliku(self, filename, folder):
        with open(filename, 'a', encoding='utf-8') as file:
            for name, attributes in folder.items():
                file.write(f"{name}: {attributes['age']}, {attributes['style']}, {attributes['mood']}\n")

    def validate_shopper_line(self, line):
        parts = [part.strip() for part in line.split(":")]

        if len(parts) < 2:
            raise ValueError(f"Invalid line '{line}'. Expected at least: name: age")

        name = parts[0]
        rest = parts[1].split(",")  # Rozdziel po przecinku

        age_text = rest[0].strip()  # Wiek

        if not name:
            raise ValueError(f"Invalid line '{line}'. Missing shopper name.")

        if not age_text.isdigit():
            raise ValueError(f"Invalid line '{line}'. Age must be a number.")

        shopper = {
            "name": name,
            "age": int(age_text),
        }

        # Opcjonalnie dodaj style i mood jeśli istnieją
        if len(rest) > 1:
            shopper["style"] = rest[1].strip()
        if len(rest) > 2:
            shopper["mood"] = rest[2].strip()

        return shopper
    def read_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            shoppers = []

            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                if not line:
                    continue

                try:
                    shoppers.append(self.validate_shopper_line(line))
                except ValueError as error:
                    raise ValueError(f"Line {line_number}: {error}") from error

            return shoppers
    def shopkeeradd(self, filename):
        folder = self.generate_data()
        print(folder)
        self.dopisz_do_pliku("shoppers.txt", folder)







