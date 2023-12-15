#!/usr/bin/env python3

"""

Sergio Vargas, 2023
sergio.vargas@lmu.de

CC-BY 4.0

"""

input_filename = './Bioinf_Basics/rosalind_revc.txt'

infile = open(input_filename, 'r')


for line in infile:
    line.rstrip()
    l = len(line)
    rev_comp = []
    for i in range(1,l+1):
        if line[l-i] == "A":
            rev_comp.append("T")
        elif line[l-i] == "T":
            rev_comp.append("A")
        elif line[l-i] == "C":
            rev_comp.append("G")
        elif line[l-i] == "G":
            rev_comp.append("C")
        else:
            print("")

print(line)
print(''.join(rev_comp))
