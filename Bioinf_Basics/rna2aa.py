#!/usr/bin/env python3

"""

Sergio Vargas, 2023
sergio.vargas@lmu.de

CC-BY 4.0

"""

codon_table = {
    "UUU":"F",
    "CUU":"L",
    "AUU":"I",
    "GUU":"V",
    "UUC":"F",
    "CUC":"L",
    "AUC":"I",
    "GUC":"V",
    "UUA":"L",
    "CUA":"L",
    "AUA":"I",
    "GUA":"V",
    "UUG":"L",
    "CUG":"L",
    "AUG":"M",
    "GUG":"V",
    "UCU":"S",
    "CCU":"P",
    "ACU":"T",
    "GCU":"A",
    "UCC":"S",
    "CCC":"P",
    "ACC":"T",
    "GCC":"A",
    "UCA":"S",
    "CCA":"P",
    "ACA":"T",
    "GCA":"A",
    "UCG":"S",
    "CCG":"P",
    "ACG":"T",
    "GCG":"A",
    "UAU":"Y",
    "CAU":"H",
    "AAU":"N",
    "GAU":"D",
    "UAC":"Y",
    "CAC":"H",
    "AAC":"N",
    "GAC":"D",
    "UAA":"x",
    "CAA":"Q",
    "AAA":"K",
    "GAA":"E",
    "UAG":"x",
    "CAG":"Q",
    "AAG":"K",
    "GAG":"E",
    "UGU":"C",
    "CGU":"R",
    "AGU":"S",
    "GGU":"G",
    "UGC":"C",
    "CGC":"R",
    "AGC":"S",
    "GGC":"G",
    "UGA":"x",
    "CGA":"R",
    "AGA":"R",
    "GGA":"G",
    "UGG":"W",
    "CGG":"R",
    "AGG":"R",
    "GGG":"G"
}

"""
split in codons. Receives a string, returns a list
"""
def GetCodons(sequence):
    codons = []
    codon = ""
    codon_position = 1
    for nt in range(0, len(sequence)):
        if (codon_position % 3) == 0:
            codon = codon + sequence[nt]
            codons.append(codon)
            codon = ""
            codon_position = 1
        else:
            codon = codon + sequence[nt]
            codon_position += 1

    return codons

"""
main
"""
input_filename = './rosalind_prot.txt'

infile = open(input_filename, 'r')

for line in infile:
    line.rstrip()
    seq_codons = GetCodons(line)
    aa_string = ""
    for i in range(0,len(seq_codons)):
        aa_string = aa_string + codon_table[seq_codons[i]]

    print(aa_string)
