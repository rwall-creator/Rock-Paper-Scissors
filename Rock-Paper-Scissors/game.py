import random

def play_game():
    valid_inputs = {"rock", "paper", "scissors"}
    count = 0

    while True:
        num_of_games = int(input("How many games did you want to play? Must be less than 20 and odd! "))
        if num_of_games % 2 != 0 and 1 < num_of_games < 20:
            print(f"Thank you for choosing {num_of_games} game(s)!")
            break
        else:
            print("Oops! Please enter a valid number!")

    best_out_of = (num_of_games // 2) + 1
    print(f"In order to win, you need to win {best_out_of} out of {num_of_games} games!")

    for i in range(num_of_games):
        while True:
            user_choice = input("Rock, paper or scissors: ").lower()
            if user_choice in valid_inputs:
                break
            else:
                print("Invalid choice, please choose rock, paper, or scissors.")

        if user_choice == "rock":
            user_num = 0
        elif user_choice == "paper":
            user_num = 1
        elif user_choice == "scissors":
            user_num = 2

        computer_choice = random.randint(0, 2)
        print(f"Computer chose {['rock', 'paper', 'scissors'][computer_choice]}!")

        if user_num == computer_choice:
            print("It's a draw!")
        elif (user_num == 0 and computer_choice == 2) or (user_num == 1 and computer_choice == 0) or (user_num == 2 and computer_choice == 1):
            print("You win this round!")
            count += 1
        else:
            print("Computer wins this round!")

        if count >= best_out_of:
            print("Congrats, you win the game!")
            break

    if count < best_out_of:
        print(f"Game over! You won {count} out of {num_of_games} games.")

    return count >= best_out_of  # Returns True if the player won the required games


def main():
    while True:
        if play_game():
            print("You won the game! Great job!")
        else:
            print("Better luck next time!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Start the game
main()