from functools import cache


def main(data):
    global garden_map
    garden_map = data
    steps = 64
    print(f"The elf could reach {fill_space(steps)} plots in {steps} steps")

    # Part 1
    # all_potential_tiles = find_all_potential_tiles(steps)
    # print(f"The elf could reach {len(all_potential_tiles)} plots in {steps} steps.")


def fill_space(steps):
    result = 0
    center_x, center_y = find_start()
    start_x = center_x - steps
    end_x = center_x + steps + 1
    y_expansion = 0
    for x in range(start_x, end_x):
        if x < center_x:
            if x == center_x and y == center_y:
                breakpoint()
            for y in range(center_y - y_expansion, center_y + y_expansion + 1, 2):
                x_translated = x % len(garden_map)
                y_translated = y % len(garden_map[0])
                if garden_map[x_translated][y_translated] != "#":
                    result += 1
            y_expansion += 1
        if x >= center_x:
            if x == center_x and y == center_y:
                breakpoint()
            for y in range(center_y - y_expansion, center_y + y_expansion + 1, 2):
                x_translated = x % len(garden_map)
                y_translated = y % len(garden_map[0])
                if garden_map[x_translated][y_translated] != "#":
                    result += 1
            y_expansion -= 1
    return result


def find_all_potential_tiles(steps=64):
    result = {find_start()}
    for x in range(steps):
        temp = []
        for tile in result:
            temp += potential_tiles(tile)
        result = set(temp)
    return result


@cache
def find_start():
    for x, line in enumerate(garden_map):
        for y, tile in enumerate(line):
            if tile == "S":
                return x, y


@cache
def potential_tiles(tile):
    result = []
    for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x = tile[0] + direction[0]
        y = tile[1] + direction[1]
        x_translated = x % len(garden_map)
        y_translated = y % len(garden_map[0])
        if garden_map[x_translated][y_translated] != "#":
            result.append((x, y))
    return result
