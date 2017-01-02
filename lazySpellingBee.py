num_tests = int(raw_input())
for test_index in range(num_tests):
    input_string = raw_input()
    num_cases_string = 1
    for char_index in range(len(input_string)):
        num_cases_char = 1
        if char_index > 0 and input_string[char_index - 1] != input_string[char_index]:
            num_cases_char += 1
        if char_index < len(input_string) - 1 and input_string[char_index + 1] != input_string[char_index]:
            num_cases_char += 1
        num_cases_string = num_cases_string * num_cases_char % 1000000007
    print("Case #{0}: {1}".format(test_index + 1, num_cases_string))
