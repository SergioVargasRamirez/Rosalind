#!/usr/bin/env python3

"""

Sergio Vargas, 2023
sergio.vargas@lmu.de

CC-BY 4.0

"""

input_filename = './Bioinf_Basics/rosalind_rna.txt'

infile = open(input_filename, 'r')

for line in infile:
    print(line.replace("T", "U"))
