## Lab 2 Exercise 3
## Generate a hollow square based on the + integer input side length n.

# Get user input for the side length

n = int(input("Enter the side length of the square: "))

for i in range(n):
    if i == 0 or i == n - 1:
        print("x" * n)
    else:
        print("x" + " " * (n - 2) + "x")