from pathlib import Path
import re

path = Path(__file__).parent / "input.txt"

output = 0

with open(path) as input_file:
    for line in input_file:
        output += int(re.search(r'\d', line).group() + re.search(r'\d', line[::-1]).group()[::-1])

print(output)