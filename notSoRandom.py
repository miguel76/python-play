num_tests = int(raw_input())
for test_index in range(num_tests):
    (num_machines, input, k, a, b, c) = map(int, raw_input().split())

    a/100 * input&k + b/100 * input|k + c/100 * input^k

    print("Case #{0}: {1}".format(test_index + 1, result))
