from pathlib import Path
import re
#import pandas as pd

path = Path(__file__).parent / "input.txt"

id_sum = 0

max_inputs = {
    "red" : 12,
    "green": 13,
    "blue" : 14
}


with open(path) as input_file:
    for line in input_file:
        can_be_played = True

        game = line.split(":")

        game_number = int(re.search(r'\d+', game[0]).group())

        for round in game[1].split(";"):
            results = dict(x.strip().split(" ") for x in round.split(","))

            for result in results:
                max = max_inputs[results[result]]

                if int(result) > int(max): 
                    can_be_played = False
                    break
            
            if not can_be_played:
                break

        if can_be_played:
            id_sum += game_number

print(id_sum)