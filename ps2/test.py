secret_word = 'apple'
letters_guessed = ['a', 'p', 'p', 'p', 'l']
def is_word_guessed(secret_word, letters_guessed):
    secret_word_split = list(secret_word)
    for letter in secret_word_split:
        if letter in letters_guessed:
            letters_guessed.remove(letter)
        else:
            return False
    return True
print (is_word_guessed(secret_word, letters_guessed))
