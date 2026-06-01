import random
word_list = ["python","operating","database","datastructure","java","javascript","computer","programming","algorithm","development"]
#1 to choose a random word from the list . var is choosenword and print
chosen_word = random.choice(word_list)
print(chosen_word)

# ask user to guess letter and store var guess
guess = input("Guess a Letter: ").lower()
print(guess)

# check if one of letter guessed is wrong
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
    