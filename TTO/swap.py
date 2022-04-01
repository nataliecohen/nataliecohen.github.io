
def swap (x,y):
    q = x
# we set one of our variables to a temporary variable
    x = y
#swap the original two variables
    y = q
#set y equal to the temp

    return x,y

def driver ():
    x = 21
y = 16
print (x,y)

a,b= swap(16,21)
print(a, b)


if __name__ == "__main__":
    driver()

