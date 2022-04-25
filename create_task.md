{% include navigation.html %}

- [Video](https://www.loom.com/share/c8275f4fe6524a16b2d1197e30d9d692) 

### Program overview:

This program will portray dashes that represent the number of letters in a certain word. Today in the world, there is a very popular game called Wordle that many people play. I decided to take the idea of wordle and create my own word guessing game. There is a selection of words that are randomly selected. The user is given no hints and just begin to enter letters that they believe could be in the word. If they are correct, the user grows one step closer to guessing the correct word, but if they are wrong the user continues to input letters until told they are correct. This program is intented to be a game/puzzle used by the user. 

#### Functionality of the Program: 
This program has the user input letters from the alphabet and the output is the letters in the correct spot, or a message telling the user they are incorrect and to continue guessing. 

```
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
    menu()
```


<div class="row justify-content-center" style="margin: 2%;">
    <iframe height="1000px" width="700px" src="https://replit.com/@NatalieCohen/Create-Task-NC?v=1?lite=true"></iframe>
</div>








