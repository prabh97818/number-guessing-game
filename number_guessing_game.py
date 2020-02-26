import random
game_over = False
while not game_over:
    ask = input("\nNew Game? (y/n): ")
    if ask == "y":
        win_number = random.randint(1,100)
        attempt = 1
        win = False
        number = int(input("Guess the number between 1 to 100: "))
        while not win:
            if number == win_number:
                print(f"YOU WIN! You guessed the right number in {attempt} attempts")
                win = True
            else:
                if number<win_number:
                    print("Too Low")
                else:
                    print("Too High")
                attempt += 1
                number = int(input("Try Again: "))
    else:
        game_over = True