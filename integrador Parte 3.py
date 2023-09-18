import os


def clear_and_print(number):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(number)


def main():
    number = 0

    while number <= 50:
        key = input("Presiona la tecla 'n' para continuar: ")

        if key == "n":
            clear_and_print(number)
            number += 1


if __name__ == "__main__":
    main()
