def half_fib(n):
    if n == 1 or n == 2:
        return 1
    elif n % 3 == 0:
        return half_fib(n - 1) + half_fib(n - 2) - 1
    else:
        return half_fib(n - 1) + half_fib(n - 2)

num_tests = int(raw_input())
for test_index in range(num_tests):
    height = int(raw_input())
    print str(half_fib(height))
