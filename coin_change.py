def greedy_min_change(value):
    coins = [1, 5, 10, 21, 25, 117, 150, 235]
    n = len(coins)

    resp = []
    for i in range(n - 1, -1, -1):
        while value >= coins[i]:
            value -= coins[i]
            resp.append(coins[i])

    return resp


if __name__ == '__main__':
    n = 2147
    resp = greedy_min_change(n)
    print(resp)
    print(len(resp))
