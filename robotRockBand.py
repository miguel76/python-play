num_tests = int(raw_input())
for test_index in range(num_tests):
    (candidates_for_position, trendy_number) = map(int, raw_input().split())
    counts = []
    for position in range(4):
        count_for_position = {}
        for candidate in map(int, raw_input().split()):
            if candidate in count_for_position:
                count_for_position[candidate] += 1
            else:
                count_for_position[candidate] = 1
        counts.append(count_for_position)

    while(len(counts) > 1):
        new_counts = []
        for index1 in range(0, len(counts), 2):
            new_counts_pair = {}
            counts1 = counts[index1]
            counts2 = counts[index1 + 1]
            for num1 in counts1:
                for num2 in counts2:
                    new_num = num1 ^ num2
                    new_count = counts1[num1] * counts2[num2]
                    if new_num in new_counts_pair:
                        new_counts_pair[new_num] += new_count
                    else:
                        new_counts_pair[new_num] = new_count
            new_counts.append(new_counts_pair)
        counts = new_counts

    result = counts[0][trendy_number] if trendy_number in counts[0] else 0

    print("Case #{0}: {1}".format(test_index + 1, result))
