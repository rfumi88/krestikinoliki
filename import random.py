import random
import os

def create_board(size):
    return [['.' for column in range(size)] for row in range(size)]

def print_board(board):
    size = len(board)
    print("  " + " ".join(str(i + 1) for i in range(size)))
    for i in range(size):
        print(f"{i + 1} " + " ".join(board[i]))

def check_win(board, player):
    size = len(board)
    for i in range(size):
        if all(board[i][j] == player for j in range(size)):  
            return True
        if all(board[j][i] == player for j in range(size)):  
            return True
    if all(board[i][i] == player for i in range(size)):
        return True
    if all(board[i][size-1-i] == player for i in range(size)):
        return True
    return False

def check_draw(board):
    for row in board:
        if '.' in row:
            return False
    return True

def save_stats(winner):
    with open("stats.txt", "a") as f:
        f.write(winner + "\n")

def show_stats():
    try:
        with open("stats.txt", "r") as f:
            games = f.readlines()
        x_wins = games.count("X\n")
        o_wins = games.count("O\n")
        draws = games.count("Ничья\n")
        total = len(games)
        print(f"\nКоличество игр: {total} | X: {x_wins} | O: {o_wins} | Ничья: {draws}")
    except:
        print("\nВы ещё ни разу не сыграли.")

def clear_stats():
    try:
        if os.path.exists("stats.txt"):
            os.remove("stats.txt")
            print("Статистика очищена!")
        else:
            print("В статистике нет данных для очистки.")
    except Exception as e:
        print(f"Ошибка очистки статистики: {e}")

def play_game():
    while True:
        try:
            size = int(input("Введите размер поля (3-9): "))
            if 3 <= size <= 9:
                break
            print("Такого размера не существует")
        except:
            print("Введите число от 3-9")
    board = create_board(size)
    current_player = random.choice(['X', 'O'])
    print(f"Первым начинает: {current_player}")
    print_board(board)
    while True:
        while True:
            try:
                move = input(f"Очередь - {current_player}: ")
                row, col = map(int, move.split())
                if 1 <= row <= size and 1 <= col <= size and board[row-1][col-1] == '.':
                    board[row-1][col-1] = current_player
                    break
                print("Неизвестное значение")
            except:
                print("Введите два числа через пробел")
        print_board(board)
        if check_win(board, current_player):
            print(f"{current_player} победил!")
            save_stats(current_player)
            break
        if check_draw(board):
            print("Ничья!")
            save_stats("Ничья")
            break
        current_player = 'O' if current_player == 'X' else 'X'

print("Крестики-нолики")
while True:
    print("1 - Запустить игру")
    print("2 - Показать статистику")
    print("3 - Очистить статистику")
    print("4 - Выход")
    choice = input("Ваш выбор: ").strip()
    if choice == '1':
        play_game()
        again = input("Хотите сыграть снова? (да/нет): ").lower()
        if again not in ['да', 'д']:
            show_stats()
            print("До следующей игры!")
            break
    elif choice == '2':
        show_stats()
    elif choice == '3':
        confirm = input("Вы уверены, что хотите очистить статистику? (да/нет): ").lower()
        if confirm in ['да', 'д']:
            clear_stats()
        else:
            print("Очистка отменена")
    elif choice == '4':
        show_stats()
        print("До следующей игры!")
        break   
    else:
        print("Неизвестный выбор.")