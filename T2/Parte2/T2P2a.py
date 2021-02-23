import sys
import os
import pefile


def print_sections(directory, executable):
    pe = pefile.PE(executable if directory is None else directory + "/" + executable)
    sections = []
    for section in pe.sections:
        sections.append(section.Name.decode('utf-8'))
    print(executable + ": [", end="")
    for i, section in enumerate(sections):
        print("'{}'".format(section), end="")
        if i < len(sections) - 1:
            print(', ', end="")
    print("]")


if os.path.isdir(sys.argv[1]):
    for filename in os.listdir(sys.argv[1]):
        if filename.endswith(".exe"):
            print_sections(sys.argv[1], filename)
else:
    print_sections(None, sys.argv[1])
