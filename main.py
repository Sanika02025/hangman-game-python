import random
word_list = ["python","operating","database","datastructure","java","javascript","computer","programming","algorithm","development"]
#1 to choose a random word from the list . var is choosenword and print
chosen_word = random.choice(word_list)
print(chosen_word)

# ask user to guess letter and store var guess

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a Letter: ").lower()


# check if one of letter guessed is wrong
display = ""


for letter in chosen_word:
    if letter == guess:
        display += letter
        
    else:
        display += "_"
print(display)