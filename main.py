# Консольний довідник з Python

def show_menu():
    print("=== Довідник Python ===")
    print("1. Показати поради")
    print("0. Вихід")

if __name__ == "__main__":
    show_menu()

name = input('Як тебе звати?')
print(f"Привіт {name}")

