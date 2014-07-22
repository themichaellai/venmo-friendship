import re
import sys
from collections import Counter
from gender_detector import GenderDetector

def file_lines(filename):
    with open(sys.argv[1]) as f:
        for line in f:
            yield line

def extract_people(line):
    match = re.match('"(.*?)" : "(.*?)"', line)
    if match:
        return frozenset(match.groups())

def are_opposite(pair, detector):
    detector = GenderDetector('us')
    tup = tuple(pair)
    for first, second in [tup, (tup[1], tup[0])]:
        if first == 'male' and second == 'female':
            return true
    return false

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('need filename')

    extracted_people = (extract_people(line) for line in file_lines(sys.argv[1]))
    print Counter(extracted_people)
