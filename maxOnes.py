num_tests = int(raw_input())
for test_index in range(num_tests):
    array_size = int(raw_input())
    array = map(int, raw_input().split())
    max_flips = int(raw_input())

    stripes = []
    gaps = []
    total_zeroes = 0
    max_stripe = 0

    firstOneFound = False
    curr_gap = 0
    curr_stripe = 0
    old_bit = 0
    for bit in array:
        if (bit == 0):
            total_zeroes += 1
            if (old_bit == 0):
                curr_gap += 1
            else:
                stripes.append(curr_stripe)
                if (curr_stripe > max_stripe):
                    max_stripe = curr_stripe
                curr_gap = 1
        else:
            if (old_bit == 0):
                if (firstOneFound):
                    gaps.append(curr_gap)
                else:
                    firstOneFound = True
                curr_stripe = 1
            else:
                curr_stripe += 1
        old_bit = bit
    if old_bit == 1:
        stripes.append(curr_stripe)
        if (curr_stripe > max_stripe):
            max_stripe = curr_stripe

#    max_stripe_available_flips = max_flips

    for start_gap_index in range(len(gaps)):
        gap_index = start_gap_index
        available_flips = max_flips
        curr_stripe = stripes[start_gap_index]
        while (gap_index < len(gaps) and gaps[gap_index] <= available_flips):
            curr_stripe += stripes[gap_index + 1]
            available_flips -= gaps[gap_index]
            gap_index += 1
        if (curr_stripe > max_stripe):
            max_stripe = curr_stripe
#            max_stripe_available_flips = available_flips

    result = max_stripe + min(max_flips, total_zeroes)

#    print("Case #{0}: {1}".format(test_index + 1, result))
    print(result)
