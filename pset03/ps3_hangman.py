# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "/home/tom/Documents/Programming/MIT_course/pset03/words.txt"

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

# end of helper code
# -----------------------------------

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    word_guessed = True
    for letter in secretWord:
      if letter not in lettersGuessed:
        word_guessed = False
    return word_guessed

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word_so_far = ""
    for letter in secretWord:
      if letter in lettersGuessed:
        word_so_far += letter
      else:
        word_so_far += "_ "
    return word_so_far

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    av_letters = "abcdefghijklmnopqrstuvwxyz"
    for x in lettersGuessed:
      if x in av_letters:
        av_letters = av_letters.replace(x, '')
    return av_letters

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
    lettersGuessed = []
    guesses_left = 8
    print("Welcome to the game, Hangman!")
    print("	I am thinking of a word that is", len(secretWord), "letters long.")
    while guesses_left > 0 and not isWordGuessed(secretWord, lettersGuessed):
      print("-------------")
      print("You have", guesses_left, "guesses left.")
      print("Available letters:", getAvailableLetters(lettersGuessed))
      guessed_letter = ""
      while len(guessed_letter) != 1:
        guessed_letter = input("Please guess a letter: ").lower()
      if guessed_letter in lettersGuessed:
        print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
      elif guessed_letter in secretWord:
        lettersGuessed.append(guessed_letter)
        print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
      else:
        lettersGuessed.append(guessed_letter)
        print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        guesses_left -= 1

    if isWordGuessed(secretWord, lettersGuessed):
	    print("Congratulations, you won!")
    else:
      print("Sorry, you ran out of guesses. The word was", secretWord, ".")


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
