#!/usr/bin/env python3

"""

Sergio Vargas, 2023
sergio.vargas@lmu.de

CC-BY 4.0

"""

input_filename = './rosalind_ini5.txt'
output_filename = './output.txt'

infile = open(input_filename, 'r')
outfile = open(output_filename, 'w')

index = 1

for line in infile:
    if index % 2 == 0:
        outfile.write(str(line) + '\n')
    index = index + 1
