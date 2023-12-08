from pathlib import Path
import regex as re

path = Path(__file__).parent / "input.txt"

REG = r'one|two|three|four|five|six|seven|eight|nine|\d'

def find_numbers(str):
    return re.findall(REG, str, overlapped=True)

WORDS_TO_NUMBERS = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'zero': '0'
        }

def convert_to_number(s):    
    if s.isnumeric():
        return s
    else:
        return WORDS_TO_NUMBERS[s]    

output = 0

with open(path) as input_file:
    for line in input_file:
        numbers = find_numbers(line)
        output += int(convert_to_number(numbers[0]) + convert_to_number(numbers[-1]))

print(output)