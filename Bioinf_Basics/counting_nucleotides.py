#!/usr/bin/env python3

"""

Sergio Vargas, 2023
sergio.vargas@lmu.de

CC-BY 4.0

"""

input_filename = './Bioinf_Basics/rosalind_dna.txt'
output_filename = './output.txt'

infile = open(input_filename, 'r')

for line in infile:
    print(str(line.count("A")))
    print(str(line.count("C")))
    print(str(line.count("G")))
    print(str(line.count("T")))
