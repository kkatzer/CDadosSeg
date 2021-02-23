import sys
import pefile
import re

# Pega os headers de um executável
def get_headers(executable):
    pe = pefile.PE(executable)
    sections = []
    for section in pe.sections:
        sections.append(section.Name.decode('utf-8'))
    return sections

# Pega os headers dos argumentos de entrada
sections1 = get_headers(sys.argv[1])
sections2 = get_headers(sys.argv[2])

# Imprime a intersecção entre as listas
commonSections = list(set(sections1).intersection(sections2))
print("Seções comuns: [", end="")
for i, section in enumerate(commonSections):
    print("'{}'".format(section), end="")
    if i < len(commonSections) - 1:
        print(', ', end="")
print("]\n")

# Imprime a diferença da lista 1 para a lista 2
difference12 = list(set(sections1).difference(sections2))
print(re.sub(".*/", "", sys.argv[1]) + ": [", end="")
for i, section in enumerate(difference12):
    print("'{}'".format(section), end="")
    if i < len(difference12) - 1:
        print(', ', end="")
print("]\n")

# Imprime a diferença da lista 2 para a lista 1
difference21 = list(set(sections2).difference(sections1))
print(re.sub(".*/", "", sys.argv[2]) + ": [", end="")
for i, section in enumerate(difference21):
    print("'{}'".format(section), end="")
    if i < len(difference21) - 1:
        print(', ', end="")
print("]\n")