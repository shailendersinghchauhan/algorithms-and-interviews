# What is fibonacci?
# Ans: A Fibonacci sequence is a sequence of integers which first two terms are 0 and 1 and all other terms of the sequence are
# obtained by adding their preceding two numbers. For example: 0, 1, 1, 2, 3, 5, 8, 13 and so on
# Function for nth Fibonacci number

def Fibonacci(n):
	if n<0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n==1:
		return 0
	# Second Fibonacci number is 1
	elif n==2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(9))

#This code is contributed by Saket Modi
