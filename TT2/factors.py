class Factors:
  def __init__(self):
    self.factorail=[1]

  def __call__(self, n):
    if n > 0:
      number = n
      print("Factors of a Given Number {0} are:".format(number))
      for value in range(1, number +1):
        if number % value == 0:
          print("{0}".format(value), end=" ")
      print()
    else:
      print("Cannot calculate")

factors_of = Factors().__call__
def driver ():
  (factors_of(44))

#test nums: 5, 8, 10, 200, 44

if __name__ == "__main__":
  driver()
