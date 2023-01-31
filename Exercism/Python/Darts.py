def score(x, y):
    xa = 0
    ya = 0
    dab = ((x-xa)**2 + (y-ya)**2)**0.5
    if dab > 10:
        score = 0
    if dab<=10 and dab>5:
        score = 1
    if dab<=5 and dab>1:
        score = 5
    if dab<=1:
        score = 10
    return score
