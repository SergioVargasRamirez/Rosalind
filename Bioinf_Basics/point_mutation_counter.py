#!/usr/bin/env python3

"""

Sergio Vargas, 2023
sergio.vargas@lmu.de

CC-BY 4.0

"""

"""
calculate the hamming distance between two sequence of equal length.
"""
def Hamming(sequence_one, sequence_two):
    hamming_distance = 0
    for i in range(0, len(sequence_one)):
        if sequence_one[i] != sequence_two[i]:
            hamming_distance += 1

    return hamming_distance

input_filename = '/home/sevra/Python/Bioinf_Basics/rosalind_hamm.txt'

infile = open(input_filename, 'r')

first_sequence = infile.readline().strip()

second_sequence = infile.readline().strip()

distance = Hamming(first_sequence, second_sequence)

print(distance)


