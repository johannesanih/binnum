"""
This is a python script that converts base10 numbers to binary numbers,
It is well commented on, so you can understand it easily.
"""

# The Base10 to Binary Converter function -- toBin()
def toBin (base10Number):
	r = [] # A list to collects the remainders

	for i in range(base10Number): # A loop enough to keep the division going until it get's to zero

		if base10Number != 0 or base10Number < 0: # A condition to check if a number provided is not zero or less than zero
			rem = base10Number%2 # Gets the remainder from a division using modulus
			divNum = int((base10Number-rem)/2) # Substracts the remainder from the main number to get an even number that will be divided by 2 which will give us the next number to divide
			base10Number = divNum # Replace the main number with the new number
			r.append(str(rem)) # Add the remainder (in string format) to the list that collects remainders
		else: # If the number is zero or less than zero or the division has gotten to zero, this breaks the loop
			break

	r.reverse() # Reverses the list of remainders, the normal way it is done when you calculate remainders
	return "".join(r) # Joins the reversed remainders in the list to give us a binary numbers and then returns it after the function is done.

# The run() function provides user interaction
def run():
	choosenBase10Number = int(input("\nNUMBER: ")) # An input field for the user to fill in a base10 number
	choosenRange = input("Should It Be A Range [Y/N]: ") # An input field for the user to choose if it meant convert only the number provided or from 0 to that number

	if choosenRange == "Y" or choosenRange == "y": # Checks if the user say "Yes" to convert from zero to that number

		for num in list(range(choosenBase10Number)): # A loop that goes through a list of numbers (0 to the number provided) and converts each of those numbers
			if num == 0: # This specially checks if a number is zero and prints out the base2 result of zero which is zero
				print("0 = 0")

			binaryNumber = toBin(num+1) # This is where every other number is converted to binary in the toBin() function and the result is stored in the binaryNumber variable
			print("%i = %s" % (num+1, binaryNumber)) # The final readable result is printed in the console

	elif choosenRange == "N" or choosenRange == "n": # Checks if the user says "No" and wants to only convert the number provided to base2
		if choosenBase10Number == 0: #This specially checks if a number is zero and prints out the base2 result of zero which is zero
			print("0 = 0")

		binaryNumber = toBin(choosenBase10Number) # This is where the number provided is converted to binary in the toBin() function and the result is stored in the binaryNumber variable
		print("%i = %s" % (choosenBase10Number, binaryNumber)) # The final readable result is printed in the console

	run() # This restarts the function to allow the user to continue base10 to base2 convertion without having to run the entire program from begining

run() # This triggers the application