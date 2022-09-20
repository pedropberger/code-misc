def steps(number):
    if number <1:
        raise ValueError("Only positive integers are allowed")
    x = 0
    while number > 1:
        if number % 2 == 0:
            x = x+1
            number = number/2
        else:
            x = x+1
            number = 3*number+1
    return x
