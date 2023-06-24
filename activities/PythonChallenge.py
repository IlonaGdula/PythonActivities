import random

def play_game():
    choices = ['r', 'p', 's']
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ").lower()
        computer_choice = random.choice(choices)

        print("You chose", get_choice_name(player_choice), ", the computer chose", get_choice_name(computer_choice))

        if player_choice == computer_choice:
            print("Both players selected", get_choice_name(player_choice) + ". It's a tie!")
        elif player_choice == 'r':
            if computer_choice == 's':
                print("Rock smashes Scissors! You win!")
                player_score += 1
            else:
                print("Paper covers Rock! You lose.")
                computer_score += 1
        elif player_choice == 'p':
            if computer_choice == 'r':
                print("Paper covers Rock! You win!")
                player_score += 1
            else:
                print("Scissors cut Paper! You lose.")
                computer_score += 1
        elif player_choice == 's':
            if computer_choice == 'p':
                print("Scissors cut Paper! You win!")
                player_score += 1
            else:
                print("Rock smashes Scissors! You lose.")
                computer_score += 1
        else:
            print("Invalid choice. Please try again.")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("Final Scores:")
    print("Computer:", computer_score)
    print("Player:", player_score)

def get_choice_name(choice):
    if choice == 'r':
        return "Rock"
    elif choice == 'p':
        return "Paper"
    elif choice == 's':
        return "Scissors"
    else:
        return "Unknown"

# Start the game
play_game()
