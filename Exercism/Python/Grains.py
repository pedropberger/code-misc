def square(number):
    if number not in range(1,65):
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)

def total():
    for i in range(2,65):
        x =+ 2**i
    return x-1
