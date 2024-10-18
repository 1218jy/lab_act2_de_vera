#A teacher named Mrs. Rivera who loved making math fun for her students. One day, a student 
#named Mia asked how to calculate powers, like (2^7). Mrs. Rivera explained, “Imagine you need 
#to multiply 2 by itself seven times. We can solve this using a python code utilizing special 
#method called recursion to solve this,”
#Can you help the class of Mrs. Rivera by providing the recursive method to calculate powers?

def recursive_exponent(base, exponent):
    if exponent == 0:
        return 1

    elif exponent < 0:
        return 1 / recursive_exponent(base, -exponent)

    else:
        return base * recursive_exponent(base, exponent - 1)

base = int(input('What is the base?'))
exponent = int(input('What is the exponent?'))
result = recursive_exponent(base, exponent)
print(f"{base}^{exponent} = {result}")