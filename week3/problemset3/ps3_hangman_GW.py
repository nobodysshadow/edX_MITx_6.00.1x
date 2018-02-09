# Hangman game
#

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    correct = 0
    for letter1 in secretWord:
        for letter2 in lettersGuessed:
            if letter1 == letter2:
                correct += 1
    return correct >= len(secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    placeholder = '_ '
    statusString = ''
    correct = False
    for letter1 in secretWord:
        for letter2 in lettersGuessed:
            if letter1 == letter2:
                correct = True
        if correct:
            statusString += letter1
        else:
            statusString += placeholder
        correct = False
    return statusString

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    remaining_letters = list(string.ascii_lowercase)
    for letter1 in string.ascii_lowercase:
        for letter2 in lettersGuessed:
            if letter1 == letter2:
                try:
                    remaining_letters.remove(letter1)
                except:
                    error_raised = True
    return ''.join(remaining_letters)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessedLetters = []
    guess = ''
    numberOfGuesses = 8
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ', len(secretWord), ' letters long.')
    while numberOfGuesses >= 1:
        print('-------------')
        print('You have ', numberOfGuesses, ' guesses left.')
        print('Available letters: ',getAvailableLetters(guessedLetters))
        guess = input('Please guess a letter: ')
        if guess in secretWord:
            if guess in guessedLetters:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, guessedLetters))
            else:
                guessedLetters += guess
                print('Good guess: ', getGuessedWord(secretWord, guessedLetters))
        else:
            if guess in guessedLetters:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, guessedLetters))
            else:
                guessedLetters += guess
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, guessedLetters))
                numberOfGuesses = numberOfGuesses - 1
        if isWordGuessed(secretWord, guessedLetters):
            print('-------------')
            print('Congratulations, you won!')
            numberOfGuesses = 0
    if numberOfGuesses <= 1:
        print('-------------')
        print("Sorry, you ran out of guesses. The word was", secretWord, '.')

wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
hangman('sea')