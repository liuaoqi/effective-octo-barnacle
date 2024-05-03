import re
f = open("input.txt", "r")

result = 0
RED, GREEN, BLUE = 12, 13, 14

# read each line in the file
for each_line in f.read().split("\n"):
    if "Game" in each_line:
        game = re.match(r"Game (?P<id>\d+)", each_line.split(":")[0])
        print(each_line.split(":")[0])
        id = game.group("id")

        cubes = re.findall(r"(?P<number>\d+) (?P<color>\w+)", each_line.split(":")[1])
        red, green, blue = 0, 0, 0
        
        is_possible = True
        for cube in cubes:
            if "red" in cube:
                red = int(cube[0])
            elif "green" in cube:
                green = int(cube[0])
            elif "blue" in cube:
                blue = int(cube[0])

            if (red > RED) or (green > GREEN) or (blue > BLUE):
                is_possible = False
        if is_possible:
            result += int(id)

f.close()