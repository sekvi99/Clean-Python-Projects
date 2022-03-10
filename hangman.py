number_of_tries = 0
number_of_lives = 5
word = 'saksofon'.lower()
hash_word = ['_' for i in range(0, len(word))]
is_not_over = True

while is_not_over:
    print('Input letter: ')
    letter = input().lower()
    while letter.isalpha() == False:
        print("You haven't passed a letter. Please try again!")
        letter = input().lower()
        
    number_of_tries += 1
    if letter in word:
        for i in range(0, len(word)):
            if letter == list(word)[i]:
                hash_word[i] = letter
                if hash_word == list(word):
                    print(hash_word)
                    print(f'Game over. You won with {number_of_tries} guesses!')
                    is_not_over = False
                else:
                    print(f'You guessed correctly, letter: {letter} was in word!')
                    print(hash_word)
                
    else:
        number_of_lives -= 1
        if number_of_lives > 0:
            print(f'The letter: {letter} was not found at the word! \n You still have {number_of_lives} lives. Good luck!')
        else:
            print(f'Game over. You lost, but at least you tried: {number_of_tries} times!')
            is_not_over = False
    
    