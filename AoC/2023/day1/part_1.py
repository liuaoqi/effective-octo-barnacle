f = open("input.txt", "r")

result = 0

for x in f:
    first_found = 0
    last = 0
    # traverse each letter in current line
    for l in x:
        if l.isdigit():
            if first_found:
                last = int(l)
            else:
                result += int(l)*10
                last = int(l)
                first_found = 1
        if str(l) == '\n':
            result += int(last)

print(result)

f.close()