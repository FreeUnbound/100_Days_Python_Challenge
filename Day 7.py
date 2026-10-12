import random
import hangman_func

print(hangman_func.logo[0])

find_word=random.choice(hangman_func.word_list)
print(find_word)

length = len(find_word)
underscore = " "
for i in range(length):
    i+=1
    underscore += "_ "
print(underscore)

game_over = False
correct=[]
lives = 6

while not game_over:
        print(f"*************** {lives}/6 Lives Left ***************")
        guess = input("Guess a letter: ").lower()
        blank = " "

        if guess in correct:
            print(f"You have already guessed the letter '{guess}'")

        for letter in find_word:
            if letter == guess:
                blank += letter
                correct.append(guess)
            elif letter in correct:
                blank += letter
            else:
                blank += "_"
        print(blank)

        if guess not in find_word:
            lives -= 1
            print(f"You guessed {guess} that's not in the word, you lost a life ")
            if lives == 0:
                game_over = True
                print("\n*****************You Lost!*****************\n")
                print(f"The word was {find_word}")

        if "_" not in blank:
            game_over = True
            print("\n*****************You Won!*****************\n")

        print(hangman_func.stages[lives])