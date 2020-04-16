"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from operator import itemgetter

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


if __name__ == '__main__':
    callers = set(map(itemgetter(0), calls))
    numbers_with_texts_out = map(itemgetter(0), texts)
    numbers_with_texts_in = map(itemgetter(1), texts)
    numbers_with_calls_in = map(itemgetter(1), calls)

    not_telemarketers = set(numbers_with_texts_out) \
        .union(numbers_with_texts_in) \
        .union(numbers_with_calls_in)

    possible_telemarketers = sorted(callers.difference(not_telemarketers))

    print("These numbers could be telemarketers: ")
    for number in possible_telemarketers:
        print(number)


