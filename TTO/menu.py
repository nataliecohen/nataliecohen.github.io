"""
Introduction to Console Programming
Writing a function to print a menu
"""

# Menu options in print statement
import time
from TT1 import fibonacci
from TT1 import list
from TT2 import factorial
from TT2 import math

def print_menu():
    print('1 -- Math' )
    print('2 -- Animation' )
    print('3 -- List' )
    print('4 -- Exit' )
    runOptions()
 
def mathMenu():
    print('1 -- Swap Numbers' )
    print('2 -- Factorial' )
    print('3 -- Fibonacci')
    print('4 -- Factors')
    print('5 -- Exit')
    runMathOptions()

# Menu options as a dictionary
menu_options = {
    1: 'Stringy',
    2: 'Ice Cream',
    3: 'Matrix',
    4: 'Swap',
    5: 'Exit',
}

# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

# menu option 1


# print ship with colors and leading spaces


# ship function, iterface into this file

# menu option 2


# print ship with colors and leading spaces
def stringy():
    print('You chose \' 1 -  Stringy\'')

def gen_tree(rows):
    # replace *s with a space in a rowsxrows matrix
    for i in range(0, rows+1):
        for j in range(0, rows-i):
            print(end=' ')
        for k in range(0, i):
            print('*', end=' ')
        print()


def driver():
    rows = int(input("Enter height of the tree:  "))
    gen_tree(rows)
    # single line lambda function
    # a is the parameter to the function
    # lambda function returns the value for # of spaces
    spaces = lambda a: int(a-2) + a % 2
    moveRt = " " * spaces(rows)
    # print the trunk of the tree
    for i in range(3):
        print(moveRt, end="###")
        print()


if __name__ == "__main__":
    driver()


      
# original ship print code
import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"



# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "    +   ")
    print(sp + "  (  )   ")
    print(SHIP_COLOR, end="")
    print(sp + "  \  / ")
    print(sp + "   \/  ")
    print(RESET_COLOR)


# ship function, iterface into this file
def IceCream():
    # only need to print ocean once
    

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        ship_print(position)  # call to function with parameter
        time.sleep(.1)


# menu option 3
def matrix():
  matrixa = [[input('1 number:'), input('2 number:'), input('3 number:')], 
             [input('4 number:'), input('5 number:'), input('6 number:')], 
             [input('7 number:'), input('8 number:'), input('9 number:')]]
  matrixb = []
  matrix1(matrixa, matrixb)
  print(matrixb)
  
def matrix1(matrixa, matrixb):
  for i in range(len(matrixa)):
      for j in range(len(matrixa[i])):
          matrixb.append(matrixa[i][j])
  return(matrixb)

def matrix2(matrixa, matrixb):
  print(matrixb[0], matrixb[1], matrixb[2])
  print(matrixb[3], matrixb[4], matrixb[5])
  print(matrixb[6], matrixb[7], matrixb[8])
  
# menu option 4
def swap():
  c = int(input('Whats your first number?:'))
  d = int(input('Whats your second number?:'))
  c,d = swap1(c,d)
  print(d,c) 

def swap1(a,b):
  if a > b:
    b, a = a, b  # swap values
  else:
    a, b = a, b
  return a, b  # return 2 values

# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-5: '))
            if option == 1:
                stringy()
            elif option == 2:
                IceCream()
            elif option == 3:
                matrix()
            elif option == 4:
                swap()
            # Exit menu    
            elif option == 5:  
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 5.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
    print_menu2()




      

    
 
           
