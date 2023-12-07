def is_valid_char(char):
    return char.isdigit() or char in "*$+#"

def get_adjacent_numbers(engine, row, col):
    adjacent_numbers = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(engine) and 0 <= new_col < len(engine[0]) and is_valid_char(engine[new_row][new_col]):
            if engine[new_row][new_col].isdigit():
                adjacent_numbers.append(int(engine[new_row][new_col]))

    return adjacent_numbers

def sum_part_numbers(engine):
    total_sum = 0

    for row in range(len(engine)):
        for col in range(len(engine[row])):
            if is_valid_char(engine[row][col]):
                adjacent_numbers = get_adjacent_numbers(engine, row, col)
                total_sum += sum(adjacent_numbers)

    return total_sum

# Example engine schematic
engine_schematic = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

result = sum_part_numbers(engine_schematic)
print(result)