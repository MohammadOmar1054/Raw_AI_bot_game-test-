import random

# Constants
BREAK_LINE = '\n'
LOG_LIMIT = 3
SUGGESTED_PASSWORD_RANGE = (1000, 1000000)

# Function to handle user login or sign-up
def user_authentication():
    ask_log_or_sign = int(input('Log in [1] or Sign Up [2]: '))
    
    if ask_log_or_sign == 1:
        login()
    else:
        sign_up()

# Function for user login
def login():
    correct_password = "mama12"
    attempt_count = 0
    
    while attempt_count < LOG_LIMIT:
        entered_password = input("Enter Your Password, LunaticXXD: ")
        if entered_password == correct_password:
            print("Login successful!")
            return
        else:
            print('INCORRECT PASSWORD!!!!!')
            attempt_count += 1
    
    print("Maximum attempts reached. Access denied.")

# Function for user sign-up
def sign_up():
    print('We first have to encrypt our conversation by allowing you to create a password')
    suggested_password = random.randint(*SUGGESTED_PASSWORD_RANGE)
    print('A suggested password: ', suggested_password)

    accept_suggestion = input("Press '0' to accept or '1' to deny the suggested password: ")
    
    if accept_suggestion == "0":
        print('Password set to:', suggested_password)
        print('Protected boys')
    elif accept_suggestion == "1":
        create_custom_password()

# Function to create a custom password
def create_custom_password():
    attempts_left = 4
    
    while attempts_left > 0:
        custom_password = input('Create a password (4-6 characters): ')
        
        if 4 <= len(custom_password) <= 6:
            print('Behold thy comrade, We are henceforth secured')
            return
        else:
            attempts_left -= 1
            print(f'Password must be between 4 and 6 characters. You have {attempts_left} attempts left.')
    
    print('All attempts exhausted. Default password set to suggested password.')

# Function to ask for the user's name
def ask_for_name():
    name_prompts = [
        "What's your name?: ",
        'What can I call you?: ',
        'Mind telling me your name?: ',
        "What's your name, pal?: ",
        "What's your name, buddy?: "
    ]
    return input(random.choice(name_prompts))

# Function to greet the user
def greet_user(name):
    greetings = [
        'I hope you are good,',
        'You look fine today,',
        "Hey,",
        "What's up,",
        'How is it going,',
        'Oh hey,',
        'Good day,'
    ]
    print(random.choice(greetings), name)

# Function to ask if the user wants to play a game
def ask_to_play():
    return input('Would you like to play a game? (y or n): ').lower() == 'y'

# Main game function
def play_game():
    game_choice = int(input('Which game would you choose to play? Same thought [1], Programming Outputs [2]: '))
    
    if game_choice == 1:
        same_thought_game()
    elif game_choice == 2:
        print('It\'s a difficult game! You will have to solve programming questions!')

# Function for the "Same Thought" game
def same_thought_game():
    replay_limit = int(input('How many times would you like to play this game?: '))
    print('You will choose a number from a range depending on the difficulty, and I will guess it ;)')
    
    difficulty = int(input('Choose your difficulty: Easy [1], Normal [2], or Hard [3]: '))
    
    if difficulty == 1:
        number_range = (1, 50)
    elif difficulty == 2:
        number_range = (1, 100)
    elif difficulty == 3:
        number_range = (1, 500)
    else:
        print('Invalid difficulty choice.')
        return
    
    play_rounds(replay_limit, number_range)

# Function to play rounds of the game
def play_rounds(replay_limit, number_range):
    for _ in range(replay_limit):
        user_pick = int(input(f'Pick a number from {number_range[0]} to {number_range[1]}: '))
        
        if user_pick < number_range[0] or user_pick > number_range[1]:
            print('That is out of the range.')
            continue
        
        ai_guess = random.randint(number_range[0], number_range[1])
        print('Your pick is:', user_pick)
        print('My guess is:', ai_guess if user_pick == ai_guess:
            victory_messages = [
                'Oh yeah! I guessed it right!',
                'Bingo!',
                'Well, well, well!',
                'Easy peasy!',
                'Here you go!',
                'Yeshhhh! I am loving it!'
            ]
            print(random.choice(victory_messages))
        else:
            defeat_messages = [
                'Uhh, better luck next time.',
                'I am pissed!',
                'Why are they so far away?',
                'So close!',
                'NOOOO!'
            ]
            print(random.choice(defeat_messages))
    
    print('You have reached the play limit you chose. Choose a longer play limit next time :)')
    goodbye_messages = [
        'See you soon, pal!',
        'Was a fun time playing with you!'
    ]
    print(random.choice(goodbye_messages))

# Main execution
if __name__ == "__main__":
    user_authentication()
    user_name = ask_for_name()
    greet_user(user_name)
    
    if ask_to_play():
        play_game()
    else:
        print('Okay, fine.') ```python
