class Item:
    def __init__(self, title):
        self.title = title
        self.is_available = True #за замовчуванням річ доступна

    def checkout(self):
        self.is_available = False #(позначити як видане)

    def return_item(self):
        self.is_available = True #(позначити як доступне)

class Book(Item):
    def __init__(self, title, author):
        super().__init__(title) 
        self.author = author 

class Magazine(Item):
    def __init__(self, title, issue_number):
        super().__init__(  title)
        self.issue_number = issue_numberYevhen

my_book = Book('Кобзар', 'Тарас Шевченко')
my_mag = Magazine('Nature', 145)

print(my_book.title, my_book.author, my_book.is_available)
my_book.checkout()
print(my_book.is_available)

print(my_mag.title, my_mag.issue_number, my_mag.is_available)