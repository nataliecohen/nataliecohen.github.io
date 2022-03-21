{% include navigation.html %}

Just Click Run! 

<div class="row justify-content-center" style="margin: 2%;">
    <iframe height="1000px" width="700px" src="https://replit.com/@NatalieCohen/nataliecohengithubio-5?lite=true#main.py"></iframe>
</div>

List/Loops assignment is under week1.py
# Week 1
***

## List/Loops

```

# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Natalie",  
               "LastName": "Cohen",  
               "DOB": "January 23",  
               "Birthplace": "San Diego",  
               "Email": "eansmm.cohen@gmail.com",  
               "Favorite_Sports":["Field Hockey","Soccer","Softball","Lacrosse", "Swimming"]  
              })  


# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"],
          InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Favorite Sports: ",
          end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(
        InfoDb[n]
        ["Favorite_Sports"]))  # join allows printing a string list with separator
    print()


# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

# for loop iterates on length of InfoDb
def printFor():
    for n in range(len(InfoDb)):
        print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def printWhile(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def printRecursive(n):
    if n < len(InfoDb):
        print_data(n)
        printRecursive(n + 1)
    return # exit condition

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

def fibonacci(a, b, n):
    if n < 5:
        c = a+b
        print(c)
        fibonacci(b,c,n+1)

def tester():
  print("For loop:")
  printFor()
  print("While loop:")
  printWhile(0)
  print("Recursive loop:")
  printRecursive(0)
tester()
  

fibonacci(1, 2, 3)

```
