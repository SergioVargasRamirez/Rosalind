#!/usr/bin/env python3

"""

Sergio Vargas, 2023
sergio.vargas@lmu.de

CC-BY 4.0

"""

input_filename = './rosalind_ini6.txt'

infile = open(input_filename, 'r')

word_counts = {}

for line in infile:
    words = line.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

for word in word_counts:
    print(word + " = " + str(word_counts[word]))
