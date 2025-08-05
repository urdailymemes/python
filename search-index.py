# Define the array
numbers = [45, 12, 88, 4, 33, 19]

# Ask the user for a number
user_input = int(input("Enter a number to find in the array: "))

# Check if the number is in the array
if user_input in numbers:
    index = numbers.index(user_input)
    print(f"The number {user_input} is at index {index}.")
else:
    print("The number is not in the array.")