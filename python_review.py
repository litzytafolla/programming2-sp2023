print("Hello world")

# this is a single line comment 
''' 
Task: 
- ask the user for one number 
- ask the user for another number 
- print the sum of their numbers 
'''

print("\n\n\n\n\n\n")
number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))

total = number_1 + number_2
print(total)

if total > 10:
	print("booooo")

elif total <= 9: 
	print("meh")

else: # must be val. 10
	print("nice. your number is 10")

for i in range(6):
	print(i)