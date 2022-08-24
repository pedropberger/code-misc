def leap_year(year):
    if year%4==0 and not year%100!=0:
        x=True
    if year%100==0 and year%400==0:
        x=True
    if year%100==0:
        if year%400!=0:
            x=False
    if year%4==0 and year%100!=0:
        x=True
    if year%400==0:
        x=True
    if year%4!=0:
        x=False
    return x
