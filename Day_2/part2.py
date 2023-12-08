from pathlib import Path
import re
#import pandas as pd

path = Path(__file__).parent / "input.txt"

total_result = 0

with open(path) as input_file:
    for line in input_file:
        can_be_played = True

        game = line.split(":")

        #game_number = int(re.search(r'\d+', game[0]).group())

        max_vals = {
            "blue" : 0,
            "red" : 0,
            "green" : 0
        }

        for round in game[1].split(";"):
            results = [x.strip().split(" ") for x in round.split(",")]

            for result in results:
                if int(result[0]) > int(max_vals[result[1]]):
                    max_vals[result[1]] = result[0]

        round_sum = 1

        for i in max_vals:
            round_sum = round_sum * int(max_vals[i])

        total_result += round_sum

print(total_result)