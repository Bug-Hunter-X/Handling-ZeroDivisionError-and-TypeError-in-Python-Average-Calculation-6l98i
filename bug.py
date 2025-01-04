def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# This will cause a ZeroDivisionError
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

# This will cause a TypeError
my_list = [1, 2, 'a']
average = calculate_average(my_list)
print(f"The average is: {average}")