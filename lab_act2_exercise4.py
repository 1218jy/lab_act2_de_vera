#Lab 2 Exercise 4
#Generate an inverted right triangle of height n.


height = int(input("Enter the height of the triangle: "))

for i in range(height, 0, -1):
    print('*' * i)