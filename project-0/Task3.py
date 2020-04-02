"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
from operator import itemgetter

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def is_bangalore_caller(call):
    return call[0][:5] == "(080)"


if __name__ == '__main__':
    bangalore_calls = list(filter(is_bangalore_caller, calls))
    bangalore_callees = map(itemgetter(1), bangalore_calls)
    area_code_pattern = re.compile(r"^\((0\d+)\)\d+$")
    mobile_pattern = re.compile(r"^([789]\d{3})\d*\s\d+$")
    codes_and_prefixes = []
    for callee in bangalore_callees:
        area_code_match = re.match(area_code_pattern, callee)
        if area_code_match:
            codes_and_prefixes.append(area_code_match.group(1))
            continue

        mobile_match = re.match(mobile_pattern, callee)
        if mobile_match:
            codes_and_prefixes.append(mobile_match.group(1))

    unique_codes_and_prefixes = sorted(set(codes_and_prefixes))
    print("The numbers called by people in Bangalore have codes:")
    for code_or_prefix in unique_codes_and_prefixes:
        print(code_or_prefix)

    total_calls = len(codes_and_prefixes)
    calls_to_080 = codes_and_prefixes.count("080")
    percent_calls_to_080 = (calls_to_080 / total_calls) * 100
    print(f"{percent_calls_to_080:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")