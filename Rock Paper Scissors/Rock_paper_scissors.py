import random
import time

def display_intro():
    intro_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠋⠈⣷⠶⠶⠶⠶⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣧⣤⣤⠤⣼⣷⣤⣄⣀⢿⠛⠛⠿⢿⣿⣷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⢀⡿⢸⡆⠀⠀⠀⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠀⠀⠀⣀⣀⣀⣀⣠⠞⠁⢸⡇⠀⠀⠀⡇⠈⠙⠻⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⠀⠀⠀⢻⡏⠉⠉⣧⠀⠀⢸⡇⠀⠀⢰⡇⠀⠀⡀⠘⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⡾⢷⣄⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣟⣛⡻⠶⢤⣼⠿⣤⣄⣸⣇⠀⢠⡇⠀⢸⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⣠⢤⣄⠀⠀⠀⠀⠀⠀
⠀⣰⠶⢶⣏⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠘⠋⠉⠉⠛⢶⣤⡀⠀⠉⠉⠙⠓⠾⠁⠀⣾⣿⣿⣿⣿⣿⣿⣿⡄⠀⢀⡼⠋⠀⠉⣷⠀⠀⠀⠀⠀
⢸⡏⠀⠀⠈⠳⣄⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠦⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠟⠁⠀⢠⡾⠃⠀⠀⠀⠀⠀
⠈⢻⣦⡀⠀⠀⠈⠳⣦⡀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀
⣴⠏⠈⠻⣦⡀⠀⠀⠈⠻⣦⡀⠀⠀⠙⢿⣿⡟⠛⠛⠛⠷⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⣠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠻⣄⠀⠀⠈⠻⣦⡀⠀⠀⠈⠻⠆⠀⠀⠀⠙⠳⣄⡀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⢀⣾⡏⠀⠀⢀⣀⣠⠤⠴⠖⠚⣆
⠀⢩⡷⣤⡀⠀⠈⠛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠆⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⢠⡿⠉⠉⠙⠻⢿⣿⠛⠋⠁⠀⠀⠀⢰⣿⡿⠷⠒⠋⠉⠁⠀⠀⠀⠀⠀⢸
⠀⣿⡄⠈⠛⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⣴⠋⠀⠀⠀⠀⢰⡄⠈⠙⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡤⠤⠖⠚⠉
⠀⠈⠻⢦⣄⠀⠙⠷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⡾⠁⠀⠀⠀⠀⠀⢸⠿⢦⡄⠀⠀⣇⣀⣠⣤⢤⣴⠖⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢷⣄⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⣇⠀⠀⠀⠀⠀⠀⡼⠀⠸⡇⠀⢸⠃⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⢻⡄⠀⠀⠀⠀⣼⠁⢀⡟⠛⠦⠾⠤⠤⠤⢤⡴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⢳⣄⢀⣼⠏⠀⠀⠀⠀⠀⠀⠸⠷⠤⢤⣄⣀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⣠⡴⠋⠀⠀⠀⠙⢿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⡵⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣶⣦⣤⠶⠞⠛⠉⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⠀⠀⢀⣤⣤⣤⣤⣤⣤⣶⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⢷⣶⣤⣤⣤⣤⣴⣶⣾⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    
    print(intro_art)
    print("\n" + "="*60)
    print("🎮 WELCOME TO ROCK PAPER SCISSORS ULTIMATE! 🎮")
    print("="*60)
    print("Get ready for an epic battle!")
    time.sleep(2)
    input("\nPress Enter to continue...")

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

# ASCII art for each option
ascii_art = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
 __      __
( _\    /_ )
 \ _\  /_ / 
  \ _\/_ /_ _
  |_____/_/ /|
  (  (_)__)J-)
  (  /`.,   /
   \/  ;   /
    | === |
"""
}

def display_choice(choice):
    print(f"\n{choice.upper()}:")
    print(ascii_art[choice])

# Display the intro when the game starts
display_intro()

while True:
    print("\n" + "="*30)
    print("ROCK PAPER SCISSORS")
    print("="*30)
    print("1 - Rock")
    print("2 - Paper") 
    print("3 - Scissors")
    print("Q - Quit")
    
    user_input = input("\nEnter your choice (1/2/3/Q): ").lower()
    
    if user_input == "q":
        break
    
    if user_input not in ["1", "2", "3"]:
        print("Invalid input! Please enter 1, 2, 3, or Q.")
        continue
    
    # Convert user input to option
    user_choice = options[int(user_input) - 1]
    
    # Computer makes random choice
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    
    # Display both choices with ASCII art
    print(f"\nYou chose:")
    display_choice(user_choice)
    
    print(f"Computer chose:")
    display_choice(computer_pick)
    
    # Determine winner
    if user_choice == computer_pick:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_pick == "scissors") or \
         (user_choice == "paper" and computer_pick == "rock") or \
         (user_choice == "scissors" and computer_pick == "paper"):
        print("🎉 You won! 🎉")
        user_wins += 1
    else:
        print("💻 Computer won! 💻")
        computer_wins += 1

print("\n" + "="*30)
print("FINAL RESULTS")
print("="*30)
print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")
total_games = user_wins + computer_wins
if total_games > 0:
    win_percentage = (user_wins / total_games) * 100
    print(f"Your win rate: {win_percentage:.1f}%")
print("Thanks for playing! Goodbye! 👋")