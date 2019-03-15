'''import string
def get_available_letters(letters_guessed):
    letters_available = list(string.ascii_lowercase)
    for letter in letters_guessed:
        try:
            letters_available.remove(letter)
        except ValueError:
            pass
    return letters_available

letters_guessed = ['e', 'i', 'k', 'p', 'r', ' ']
# print (get_available_letters(letters_guessed))
string1 = ''
print(string1)
letters_guessed.append(string1)
print(letters_guessed)
'''
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special
        symbol _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    if len(my_word) != len(other_word):
        return False
    for letter in my_word:
        if letter in other_word or letter == '_':
            continue
        else:
            return False
    return True

print(match_with_gaps('app_f', 'apple'))
