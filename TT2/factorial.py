class Factorial:
  def __init__(self):
        self.factorial = [1,1]
    
def fact(): 
	num = input("enter a number : ") 
	fact = 1 
	i = 1 
	while i <= int(num): 
		fact = fact * i 
		i=i+1 
	 
	print ("factorial of the number : %d" %fact) 
 
fact() 

      
