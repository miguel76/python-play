def half_fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        sum = (half_fib(n - 1) + half_fib(n - 2)) % 1000000007
        if n % 3 == 0:
            return sum - 1
        else:
            return sum

FIVE_SQUARED = 5 ** 0.5
FI = (1 + FIVE_SQUARED) / 2
PSI = (1 - FIVE_SQUARED) / 2

def half_fib2(n):
    fib = (FI ** n - PSI ** n) / FIVE_SQUARED % 2000000014
    return (int(round(fib)) + 1) // 2

num_tests = int(raw_input())
for test_index in range(num_tests):
    height = int(raw_input())
    print(str(half_fib2(height)))
