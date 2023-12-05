import sys, os

# Get Game ID
# subtract each of each color from the appropriate category
# if color goes below 0, not possible and skip


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    lines = [line.rstrip() for line in f.readlines()]
    sum_ids = 0
    def process_game(game_id, game):


        for draw in game:
            color_dict = {"red": 12, "green": 13, "blue": 14}
            for c in draw.split(","):
                number, color = c.split(" ")[1::]
                # print(number)
                curr_value = color_dict[color]
                rep = {color: curr_value - int(number)}
                color_dict.update(rep)
            print(color_dict)
            for key in color_dict.keys():
                if color_dict[key] < 0:
                    return False
        return True

    for line in lines:

        game_id = line.split(" ")[1].split(":")[0]
        game_input = line.split(":")[1].split(";")

        outcome = process_game(game_id, game_input)
        if outcome:
            sum_ids += int(game_id)

    print(f"Part 1 {sum_ids}")
