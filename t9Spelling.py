CHAR_ENCODING = {
    "a": "2", "b": "22", "c": "222",
    "d": "3", "e": "33", "f": "333",
    "g": "4", "h": "44", "i": "444",
    "j": "5", "k": "55", "l": "555",
    "m": "6", "n": "66", "o": "666",
    "p": "7", "q": "77", "r": "777", "s": "7777",
    "t": "8", "u": "88", "v": "888",
    "w": "9", "x": "99", "y": "999", "z": "9999",
    " ": "0"
}

def convert(c):
    return CHAR_ENCODING[c]

num_tests = int(raw_input())
for test_index in range(num_tests):
    result = ""
    lastDigit = "a"
    for encoding in map(convert, raw_input()):
        if encoding[0] == lastDigit:
            result += " "
        result += encoding
        lastDigit = encoding[0]
    print("Case #{0}: {1}".format(test_index + 1, result))
