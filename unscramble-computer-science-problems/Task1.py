"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from functools import reduce
from operator import concat

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
if __name__ == '__main__':
    numbers = [[text[0], text[1]] for text in texts] + [[call[0], call[1]] for call in calls]
    numbers = reduce(concat, numbers)
    numbers = set(numbers)
    number_count = len(numbers)
    print(f"There are {number_count} different telephone numbers in the records")
