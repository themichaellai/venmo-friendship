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

def are_opposite(first, second):
    detector = GenderDetector('us')
    for first, second in [(first, second), (second, first)]:
        if detector.guess(first) == 'male' and detector.guess(second) == 'female':
            return True
    return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('need filename')

    extracted_people = (extract_people(line) for line in file_lines(sys.argv[1]))
    for (first, second), v in Counter(extracted_people).iteritems():
        print '%s & %s : %d %s' % (first, second, v, are_opposite(first, second))
