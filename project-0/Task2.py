"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from itertools import groupby
from operator import itemgetter

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def call_duration_dict():
    """
    Produces a dictionary where:
        key is a phone number
        value is the total duration the number was either on an incoming or outgoing call
    """
    call_durations = {}
    for outgoing, call in groupby(numbers, key=itemgetter(0)):
        if outgoing not in call_durations:
            call_durations[outgoing] = []
        else:
            call_durations[outgoing] += list(call)

    for incoming, call in groupby(numbers, key=itemgetter(1)):
        if incoming not in call_durations:
            call_durations[incoming] = []
        else:
            call_durations[incoming] += list(call)

    total_call_durations = {}
    for call, calls_for_number in call_durations.items():
        durations = [int(call[1]) for call in calls_for_number]
        duration = sum(durations)
        total_call_durations[call] = duration

    return total_call_durations


if __name__ == '__main__':
    numbers = [[call[0], call[3]] for call in calls]

    total_durations = call_duration_dict()
    longest_caller = max(total_durations.items(), key=itemgetter(1))
    print(f"{longest_caller[0]} spent the longest time, {longest_caller[1]} seconds, on the phone during September 2016.")
