def convert(number):
    x=''
    if number%3!=0 and number%5!=0 and number%7!=0:
        return str(number)
    elif not number%3!=0:
        x='Pling'
    else:
        x=''
    if not number%5!=0:
        y='Plang'
    else:
        y=''
    if not number%7!=0:
        z='Plong'
    else:
        z=''
    listOfStrings = [x, y, z]
    return "".join(listOfStrings)
