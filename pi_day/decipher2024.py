# Welcome, Agent!
# You've intercepted a secret message encoded using a shift cipher related to the digits of pi.
# Your mission, should you choose to accept it, is to decode this message and unveil the truth hidden within.

# Part 1: Decipher the Message
# Implement an algorithm that decipher a message using the pi key. The key consist on the first 16 numbers of
# the constant Pi. Each letter of the message is shifted by the digit of the key placed in the same position.
# Blank spaces and non-letter characters are not shifted, but still part of the message. After the first 16 
# positions in the message, the shift restarts with the first digit of the key.

# Enconded Message:
# Wii kxtszof ova fsegyrpm d lnsrjkujvq roj! Kdaxii svw vnwhj pvugho buynkx tn vwh-gsvw ruzqia. Mrq'x kxtmjw bx fhlhlujw cjoq! Hmg tyhfa gx dwd fdqu bsm osynbn oulfrex, kahs con vjpmd qtjv bx whwxssp cti hmulkudui f Jgusd Yp Gdz!

# Part 2: Find the Secret Numerical Code
# Once you've deciphered the message, your next task is to find a hidden secret numerical code. Within the message,
# between the words (even between separated words by blank spaces, commas or dots), a series of numbers (from one to ten)
# written in text are concealed. The challenge requires you to calculate the multiplication of all the digits contained in the message.

# Example
# In the text We need to waterprooF OUR boots to meet the virtuoSI Xylophonists are hidden the numbers 4 and 6. Multiplying both you 4 * 6 = 24.

import math

secret = "Wii kxtszof ova fsegyrpm d lnsrjkujvq roj! Kdaxii svw vnwhj pvugho buynkx tn vwh-gsvw ruzqia. Mrq'x kxtmjw bx fhlhlujw cjoq! Hmg tyhfa gx dwd fdqu bsm osynbn oulfrex, kahs con vjpmd qtjv bx whwxssp cti hmulkudui f Jgusd Yp Gdz!"

alphabet = list(map(chr, range(ord('a'), ord('z')+1)))

# store the first 16 digits of pi into a list to traverse
pi = []
i = 0
while i < 16:
    pi.append(int(math.pi*10**i)%10)
    i += 1

# shift the letters based on the digits
secret_num = []
for letter in secret:
    if letter == " ":
        secret_num.append(float('-inf'))
    else:
        secret_num.append(ord(str.lower(letter)) - 97)

# Should shift backwards, "Wii"->"The"
# each letter should be moved backwards by corresponding digits
shifted_num = []
result = ""
i = 0
for curr in secret_num:
    digit = pi[i]
    shifted = curr - digit
    if shifted < 0:
        shifted = 26 + shifted
    shifted_num.append(shifted)

    # convert into letters
    if shifted < 0:
        result += " "
    else:
        result += alphabet[shifted]

    i += 1
    if i == 16:
        i = 0

print(result)

# the formula for crafting a delightful pie  cutoff our three golden apples of one four pounds  don t forget to weighten well  add sugar as you want and invite friends  even the silly ones to network and celebrate a happy pi day

# Part 2: now calculate

import re
# pattern = r"(one|two|three|four|five|six|seven|eight|nine|ten|\d)"
# all_num = re.findall(pattern, result.replace(" ", ""))

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
text = result.replace(" ", "")
result = []
for digit in digits:
    result += re.findall(digit, text)

# print(result)
