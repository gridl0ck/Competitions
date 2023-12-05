import sys, os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    lines = [line.rstrip().lower() for line in f.readlines()]
    first = 0
    second = 0

    def first_func(line):
        beg = None
        end = None

        for c in line:
            if c.isdigit():
                beg = c
                break

        for c in line[::-1]:
            if c.isdigit():
                end = c
                break
        return int(beg + end)

    def second_func(line):
        soln_dict = {}
        possible_values = [
             "one",
             "two",
             "three",
             "four",
             "five",
             "six",
             "seven",
             "eight",
             "nine",
             "1",
             "2",
             "3",
             "4",
             "5",
             "6",
             "7",
             "8",
             "9"
                ]

        for key in possible_values:

            found = [i for i in range(len(line)) if line.startswith(key, i)]

            if found:
                print(f"Item {key} found at {found}")
                for item in found:
                    soln_dict[item] = key

        print(line)
        sorted_soln_dict = sorted(soln_dict.items())
        soln = (sorted_soln_dict[0], sorted_soln_dict[-1])
        print(sorted_soln_dict)
        num_str = ""
        for tup in soln:
            try:
                working = tup[1]
                int(working)
                num_str += working
            except:
                value = str(possible_values.index(tup[1]) + 1)
                num_str += value

        print(num_str)
        print("-----------")

        return int(num_str)
    for line in lines:

        first += first_func(line)
        second += second_func(line)

    print(f"First function: {first}")
    print(f"Second function: {second}")