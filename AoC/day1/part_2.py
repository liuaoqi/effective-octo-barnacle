import re

f = open("input.txt", "r")

pattern = r"(one|two|three|four|five|six|seven|eight|nine|\d)"
pattern_re = r"(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)"
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

result = 0
for x in f.read().split("\n"):

    first = re.findall(pattern, x)
    if len(first) > 0:
        # the first number in the current line
        first = first[0]
        # the last number in the current line
        last = re.findall(pattern_re, x[::-1])[0][::-1]

        if first.isdigit():
            result += int(first)*10
        else:
            result += int(numbers[first])*10
        if last.isdigit():
            result += int(last)
        else:
            result += int(numbers[last])

print(result)

f.close()