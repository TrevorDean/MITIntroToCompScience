import string
def get_available_letters(letters_guessed):
    letters_available = list(string.ascii_lowercase)
    for letter in letters_guessed:
        letters_available.remove(letter)
    return letters_available

letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
print (get_available_letters(letters_guessed))

