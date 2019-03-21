# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:
# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
warnings_remaining = 3
secret_word = 'apple'  # Remove this when done testing!!!


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
      letters_guessed: list (of letters), which letters have been guessed so
      far. Assumes that all letters are lowercase.
    returns: boolean, True if all the letters of secret_word are in
    letters_guessed; False otherwise
    '''
    secret_word_split = list(secret_word)
    for letter in secret_word:
        if letter in letters_guessed:
            continue
        else:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that
    represents which letters in secret_word have been guessed so far.
    '''
    secret_word_split = list(secret_word)
    secret_word_decoded = ''
    for letter in secret_word_split:
        if letter in letters_guessed:
            secret_word_decoded += letter
        else:
            secret_word_decoded += '_ '
    return secret_word_decoded


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which
    letters have not yet been guessed.
    '''
    letters_available = list(string.ascii_lowercase)
    for letter in letters_guessed:
        try:
            letters_available.remove(letter)
        except ValueError:
            pass
    letters_available = ''.join(letters_available)
    return letters_available


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    This function gets input, verifies if the input is in the right format,
    then based on what the input is, takes away guesses then loops or just loops.
    It decides if you won and your score or it tells you you lost.
    '''
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters '
          'long.'.format(len(secret_word)))
    print('---------------------------------------')

    while guesses_remaining > 0:
        print('You have {} guesses left'.format(guesses_remaining))
        print('Available letters: {}'.format(get_available_letters(
                                             letters_guessed)))
        # Getting Input and Controlling Warnings
        guess_a_letter = input('Please guess a letter: ')
        guess_a_letter = str.lower(guess_a_letter)
        if not str.isalpha(guess_a_letter):
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print('''Oops! That is not a valid letter and you have no warnings
left so you lose one guess: ''',
                      get_guessed_word(secret_word, letters_guessed))
                continue
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print('''Oops! That is not a valid letter. You have {} warnings left:
'''.format(warnings_remaining), get_guessed_word(secret_word, letters_guessed))
                continue
        if guess_a_letter in letters_guessed:
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print('''Oops! You've already guessed that letter and you have
0 warnings left so you lose one guess: ''',
                      get_guessed_word(secret_word, letters_guessed))
                continue
            if warnings_remaining > 0:
                warnings_remaining -= 1
            print('''Oops! You've already guessed that letter.
You now have {} warnings: '''.format(warnings_remaining),
                  get_guessed_word(secret_word, letters_guessed))
            continue
        if
        # Win and Loss Conditions
        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!')
            break
        if guesses_remaining == 0:
            print('Sorry, you ran out of guesses. The word was', secret_word)
        print('---------------------------------------')


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
    counter = 0
    for letter in my_word:
        if letter == other_word[counter] or letter == '_':
            counter += 1
        else:
            return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches
    my_word Keep in mind that in hangman when a letter is guessed, all the
    positions at which that letter occurs in the secret word are revealed.
    Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # Removing white space
    my_word = ''.join(my_word.split())
    counter = 0
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word)
            counter += 1
    if counter == 0:
        print('No matches found')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the
      user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    pass
'''
    if guess_a_letter == '*':
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        continue
'''
# When you've completed your hangman_with_hint function, comment the two
# similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

# show_possible_matches('a_ _ l_')


if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    hangman(secret_word)
    ###############
    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
