'''
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''
f = open("input.txt", "r")

# result = 0

# for x in f:
#     first_found = 0
#     last = 0
#     # traverse each letter in current line
#     for l in x:
#         if l.isdigit():
#             if first_found:
#                 last = int(l)
#             else:
#                 result += int(l)*10
#                 last = int(l)
#                 first_found = 1
#         if str(l) == '\n':
#             result += int(last)


# print(result)

'''
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
'''
# class Number:
#     def __init__(self, node, digit):
#         self.node = node
#         self.digit = digit
    
#     def compare_text(self, target):
#         # -> (boolean, int)
#         # a boolean representing the comparison result,
#         # int indicating the length of string compared
#         me = self.node.get_all()

#         if target.isdigit():
#             return (self.digit == int(target), 1)
#         if target[0].isdigit():
#             return (self.digit == int(target[0]), 1)
#         if len(target) < len(me):
#             if target.isdigit():
#                 return (self.digit == int(target), 1)
#             return (False, len(target))
#         if me == target[:len(me)]:
#             return True, len(me)
#         return False, len(me)

#     def __str__(self):
#         return self.node.get_all() + ": " + str(self.digit)

# class Node:
#     def __init__(self, curr, next=None):
#         self.curr = curr
#         self.next = next
    
#     def get_all(self):
#         result = self.curr
#         next = self.next
#         while next is not None:
#             result += next.curr
#             next = next.next
#         return result

#     def __str__(self):
#         return self.get_all()

# def create_node(text):
#     return Node(text[0], create_node(text[1:]) if len(text) > 1 else None)

# numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
# num_list = []
# for x in numbers.keys():
#     num_list.append(Number(create_node(x), numbers[x]))

import re

string = "two1nine"
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

    # print(x, first, last, result)

print(result)

f.close()