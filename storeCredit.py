def best_pair(credit, num_items, item_costs):
    for index_a in range(num_items - 1):
        cost_a = item_costs[index_a]
        for index_b in range(index_a + 1, num_items):
            cost_b = item_costs[index_b]
            if cost_a + cost_b == credit:
                return (index_a, index_b)

num_tests = int(raw_input())
for test_index in range(num_tests):
    credit = int(raw_input())
    num_items = int(raw_input())
    item_costs = map(int, raw_input().split())
    result_pair = best_pair(credit, num_items, item_costs)
    print("Case #{0}: {1} {2}".format(test_index + 1, result_pair[0] + 1, result_pair[1] + 1))
