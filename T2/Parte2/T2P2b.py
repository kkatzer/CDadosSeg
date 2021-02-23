import sys
import pefile
import re


def get_headers(executable):
    pe = pefile.PE(executable)
    sections = []
    for section in pe.sections:
        sections.append(section.Name.decode('utf-8'))
    return sections


sections1 = get_headers(sys.argv[1])
sections2 = get_headers(sys.argv[2])

commonSections = list(set(sections1).intersection(sections2))
print("Seções comuns: [", end="")
for i, section in enumerate(commonSections):
    print("'{}'".format(section), end="")
    if i < len(commonSections) - 1:
        print(', ', end="")
print("]\n")

difference12 = list(set(sections1).difference(sections2))
print(re.sub(".*/", "", sys.argv[1]) + ": [", end="")
for i, section in enumerate(difference12):
    print("'{}'".format(section), end="")
    if i < len(difference12) - 1:
        print(', ', end="")
print("]\n")

difference21 = list(set(sections2).difference(sections1))
print(re.sub(".*/", "", sys.argv[2]) + ": [", end="")
for i, section in enumerate(difference21):
    print("'{}'".format(section), end="")
    if i < len(difference21) - 1:
        print(', ', end="")
print("]\n")