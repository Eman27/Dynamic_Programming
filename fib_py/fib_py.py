def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_memo(n-1) + fib_memo(n - 2)
    return memo[n]

def fib_tabu(n):
    table = [0]*(n+1)
    table[1] = 1
    for i in range(n):
        if i+1 <= n: table[i+1] += table[i]
        if i+2 <= n: table[i+2] += table[i]
    return table[n]

def main():
    #print(fib_memo(1))
    #print(fib_memo(4))
    #print(fib_memo(8))
    print(fib_memo(50))
    print(fib_tabu(50))

if __name__ == "__main__":
    main()