import random

# findLetter - loop through word to find letter
def findLetter(guess, word):
    letterIndex = -1
    for letter in word:
      if guess == letter:
          letterIndex = word.index(letter)
    return letterIndex

wordlist = ['disneyland','reads',\
            'orange','heart',\
            'life','time', \
            'pig','texts']

#Obtain random word
randWord = random.choice(wordlist)

#Determine length of random word and display number of blanks
blanks = '_ ' * len(randWord)
print()
print("Word: ", blanks)
#print(randWord)

# Keep count of letter found
foundLetterCount = 0

#Obtain guess
while True:
    print()
    guess = input("Please make a guess: ")
    if len(guess) != 1:
        print("Please guess one letter at a time!")
        continue
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print("Please only guess letters!")
        continue

    #Check if guess is found in random word
    letterIndex = findLetter(guess, randWord)
    if letterIndex == -1:
        print("Guess is wrong!")
    else:
        # Increment found letter count
        foundLetterCount = foundLetterCount + 1
        # Update blanks to display letter found
        blanks = blanks[:letterIndex * 2] + guess + blanks[letterIndex * 2 + 1:]
        print("Guess is correct!")
    print()
    print("Word: ", blanks)

    # If all letter have been found, break out of the loop.
    if foundLetterCount == len(randWord):
      print("NICE WORK!!! You guessed it")
      break

print("Please run program again to play")
