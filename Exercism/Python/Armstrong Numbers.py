# First soluction

def is_armstrong_number(number):
    aux = list(str(number))
    aux = list(int(item) for item in aux)
    l = int(len(str(number)))
    pow=sum(list(num**l for num in aux))
    return pow == number
