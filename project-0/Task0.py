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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
if __name__ == '__main__':
    texts_ascending = sorted(texts, key=itemgetter(2))
    calls_descending = sorted(calls, key=itemgetter(2), reverse=True)

    first_text = texts_ascending[0]
    last_call = calls_descending[0]

    print(f"First record of texts, {first_text[0]} texts{first_text[1]} at time {first_text[2]}")
    print(f"Last record of calls, {last_call[0]} calls {last_call[1]} at time {last_call[2]}, lasting {last_call[3]} seconds")
