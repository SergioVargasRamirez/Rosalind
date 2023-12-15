#!/usr/bin/env python3

"""

Sergio Vargas, 2023
sergio.vargas@lmu.de

CC-BY 4.0

"""

import re

def FastaReader(fasta_file):
    sequences = {}
    fasta_header = ""
    for line in infile:
        line = line.strip()
        if re.search(r"^>.+", line):
            sequences[line] = ""
            fasta_header = line
        else:
            #print(line)
            sequences[fasta_header] += line

    return sequences

def CountGC(sequence):
    Gs = sequence.count("G")
    Cs = sequence.count("C")
    return Gs + Cs

input_filename = '/home/sevra/Python/Bioinf_Basics/rosalind_gc.txt'

infile = open(input_filename, 'r')

fastas = FastaReader(infile)

max_GC = 0
max_GC_sequence = ""

for i in fastas:
    seq_GC = CountGC(fastas[i])/len(fastas[i])
    if seq_GC > max_GC:
        max_GC = seq_GC
        max_GC_sequence = i

print(max_GC_sequence + " = " + str(max_GC))


