def pd_binary_knapsack(W, wt, values, n):
    matriz = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                matriz[i][w] = 0
            elif wt[i - 1] <= w:
                matriz[i][w] = max(values[i - 1] + matriz[i - 1]
                                   [w - wt[i - 1]],  matriz[i - 1][w])
            else:
                matriz[i][w] = matriz[i - 1][w]

    return matriz[n][W]


values = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print(pd_binary_knapsack(W, wt, values, len(values)))
