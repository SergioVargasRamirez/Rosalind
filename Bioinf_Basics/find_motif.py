#!/usr/bin/env python3

"""

Sergio Vargas, 2023
sergio.vargas@lmu.de

CC-BY 4.0

"""

"""
get a kmer table from a sequence of interest
"""
def GetKmers(sequence, k):
    kmers = []
    for nt in range(0, len(sequence)):
        if k <= (len(sequence) - nt):
            kmers.append(sequence[nt:(nt+k)])
    return kmers

"""
main
"""

input_filename = './rosalind_subs.txt'
infile = open(input_filename, 'r')

sequence = infile.readline().rstrip()
motif = infile.readline().rstrip()

print(motif)

seq_kmers = GetKmers(sequence, len(motif))
for i in range(0, len(seq_kmers)):
    if seq_kmers[i] == motif:
        print(i+1)

