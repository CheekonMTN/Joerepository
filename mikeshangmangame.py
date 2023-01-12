import random
import string



# Function that gets the word that has to be guessed by the user

def get_new_word() -> str:
    with open("usa.txt") as file:
        file_raw: str = file.read()
        dictionary: list = file_raw.split("\n")
        length_of_file: int = len(dictionary)
        line_selection: int = random.randint(0, length_of_file-1)
        word_selection: str = dictionary[line_selection]

        return word_selection

# Function for displaying current progress on the word

def gen_word_output(answer: str, guesses: list[str]) -> str:
    output: str = ""
    for letter in answer:
        if letter in guesses:
            output = output + letter
        else:
            output = output + "-"
    return output
# Function for displaying how many lives are left

def gen_lives_output(lives_remaining: int) -> str:
    return str(lives_remaining) + " lives remaining"

# Function for displaying which letters have been guessed
def gen_guesses_output(guesses: list[str]) -> str:

    return "guessed so far : " + ", ".join(guesses)


# Function that displays current progress/ lives left/ letters guessed to the user
def gen_output(answer: str, lives: int, guesses: list[str]) -> str:
    word_output: str = gen_word_output(answer, guesses)
    lives_output: str = gen_lives_output(lives) 
    guesses_output: str = gen_guesses_output(guesses)
    # return word_output + " | " + lives_output + " | " + guesses_output
    return " | ".join([word_output, lives_output, guesses_output])

# Gameplay logic
    
def gameplay(word):

    number_of_lives: int = 10
    game_won: str = False
    guessed_letters: list = []
    alphabet: list = list(string.ascii_lowercase)
    selected_word_for_game: str = word
    
    print("Let's play some hangman!")
    print(gen_word_output(selected_word_for_game, guessed_letters))
    print("This is how many lives you start with - " + str(number_of_lives))
    print("\n")
    
    while not game_won and number_of_lives > 0:
        
        user_guess: str = input("Please type your guess: ")
        if "-" not in gen_word_output(selected_word_for_game, guessed_letters):
            current_progress: str = gen_output(selected_word_for_game, number_of_lives, guessed_letters)
            game_won = True
            break
        #  Checking if the user's guess was correct, already guessed, or incorrect. If a word or multiple letters is input an error occurs
        if len(user_guess) != 1 or user_guess not in alphabet:
            print("not a valid entry. Please try again.")
            current_progress: str = gen_output(selected_word_for_game, number_of_lives, guessed_letters)
            print(current_progress)
            continue
            # if user_guess was used already
        if user_guess in guessed_letters:
            print("You have already guessed that letter! Try again.")
            current_progress: str = gen_output(selected_word_for_game, number_of_lives, guessed_letters)
            print(current_progress)
            continue
        if user_guess not in selected_word_for_game:
            print(user_guess, "is not in the word. Try again!")
            number_of_lives -= 1
            guessed_letters.append(user_guess)
            current_progress: str = gen_output(selected_word_for_game, number_of_lives, guessed_letters)
            print(current_progress)
            continue
            
        # if user_guess is in the word, guessed_letters list is updated
        else: 
            print(user_guess, "is in the word!")
            guessed_letters.append(user_guess)
            current_progress: str = gen_output(selected_word_for_game, number_of_lives, guessed_letters)
            print(current_progress)
            continue
    
    
        
    # Game won or lost
    if game_won == True:
        print("Good job, you won! The word was " + selected_word_for_game)
        
    else:
        print("You're out of lives! You're DEAD! The correct word was " + selected_word_for_game)

# Function that runs the game
def main():
    word = get_new_word()
    gameplay(word)

main()
