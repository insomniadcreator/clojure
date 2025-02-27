
range_start = 0
range_end = 0
current_guess = 0


def start(n, m):
    global range_start, range_end, current_guess
    range_start = n
    range_end = m
    current_guess = (n + m) // 2
    print("Я готов...")


def guess_my_number():
    return current_guess


def smaller():
    global range_end, current_guess
    range_end = current_guess - 1
    current_guess = (range_start + range_end) // 2
    return current_guess


def bigger():
    global range_start, current_guess
    range_start = current_guess + 1
    current_guess = (range_start + range_end) // 2
    return current_guess


def play_game():
    print("Добро пожаловать в игру 'Угадай число' наоборот!")
    n = int(input("Введите начало диапазона: "))
    m = int(input("Введите конец диапазона: "))
    start(n, m)

    while True:
        print(f"Моё предположение: {guess_my_number()}")
        response = input("Ваше число (больше/меньше/угадал)? ").strip().lower()

        if response == "угадал":
            print("Ура! Я угадал!")
            break
        elif response == "меньше":
            smaller()
        elif response == "больше":
            bigger()
        else:
            print("Пожалуйста, введите 'больше', 'меньше' или 'угадал'.")


if __name__ == "__main__":
    play_game()