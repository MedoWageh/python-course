# Function to print the multiplication table
def print_multiplication_table(n):
    # Loop through numbers 1 to 10
    for i in range(1, 11):
        # Print the multiplication result
        print(f"{n} x {i} = {n * i}")

# Example usage:
number = 6
print(f"Multiplication table for {number}:")
print_multiplication_table(number)
