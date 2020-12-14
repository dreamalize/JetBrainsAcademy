import random
random.seed()


# Main Function
def change_word(word, secret_word, letter):
    list_secret_word = list(secret_word)     # word_on_screen divided into elements of list
    letter_counter = word.count(letter)      # How many times user_letter appears in win word
    ind = -1                                 # decrease index by one, because next step we use index + 1
    for times in range(letter_counter):
        ind = word.find(letter, ind + 1)     # looking for index every coincidence of user_letter
        list_secret_word[ind] = letter
        ind += 1
    secret_word = ""                         # clear secret_word and rebuild it from changed list of word_on_screen
    for i in list_secret_word:
        secret_word += i
    return secret_word


# Conditions of the game
words_for_game = ["python", "java", "kotlin", "javascript"]  # list of the words computer chooses
win_word = random.choice(words_for_game)                     # chosen word
word_on_screen = "-" * len(win_word)                         # starting word on screen
attempts = 8                                                 # number of possible attempts
user_inputs = []


# Start of the game
print("H A N G M A N")
menu = []
while True:
    menu_input = input("""Type "play" to play the game, "exit" to quit: """)
    menu.append(menu_input)
    if menu[-1] == "exit":
        break
    elif menu[-1] == "play":
        while attempts > 0:
            if word_on_screen == win_word:
                break
            print()
            print(word_on_screen)
            user_letter = input("Input a letter: ")

            # checking correct input
            if len(list(user_letter)) != 1:
                print("You should input a single letter")
            elif not user_letter.islower():
                print("Please enter a lowercase English letter")
            elif user_letter in user_inputs:
                print("You've already guessed this letter")

            # the game
            elif user_letter in win_word:
                word_on_screen = change_word(win_word, word_on_screen, user_letter)
                user_inputs.append(user_letter)
            else:
                attempts -= 1
                print("That letter doesn't appear in the word")
                user_inputs.append(user_letter)

        # Exit of the game
        if word_on_screen == win_word:
            print("You guessed the word")
            print("You survived!")
            print()
        else:
            print("You lost!")
            print()
