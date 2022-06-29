def weightedMean(X, W):
    sum_items = 0
    for i in range(n):
        sum_items = sum_items + (vals[i] * weights[i])
    print(round(sum_items/sum(weights), 1))
