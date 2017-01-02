num_tests = int(raw_input())
for test_index in range(num_tests):
    print("Case #{0}: {1}".format(test_index + 1, " ".join(raw_input().split()[::-1])))
