#!/usr/bin/env python3

"""

Sergio Vargas, 2023
sergio.vargas@lmu.de

CC-BY 4.0

"""

import re

codon_table = {
    "TTT":"F",
    "CTT":"L",
    "ATT":"I",
    "GTT":"V",
    "TTC":"F",
    "CTC":"L",
    "ATC":"I",
    "GTC":"V",
    "TTA":"L",
    "CTA":"L",
    "ATA":"I",
    "GTA":"V",
    "TTG":"L",
    "CTG":"L",
    "ATG":"M",
    "GTG":"V",
    "TCT":"S",
    "CCT":"P",
    "ACT":"T",
    "GCT":"A",
    "TCC":"S",
    "CCC":"P",
    "ACC":"T",
    "GCC":"A",
    "TCA":"S",
    "CCA":"P",
    "ACA":"T",
    "GCA":"A",
    "TCG":"S",
    "CCG":"P",
    "ACG":"T",
    "GCG":"A",
    "TAT":"Y",
    "CAT":"H",
    "AAT":"N",
    "GAT":"D",
    "TAC":"Y",
    "CAC":"H",
    "AAC":"N",
    "GAC":"D",
    "TAA":"x",
    "CAA":"Q",
    "AAA":"K",
    "GAA":"E",
    "TAG":"x",
    "CAG":"Q",
    "AAG":"K",
    "GAG":"E",
    "TGT":"C",
    "CGT":"R",
    "AGT":"S",
    "GGT":"G",
    "TGC":"C",
    "CGC":"R",
    "AGC":"S",
    "GGC":"G",
    "TGA":"x",
    "CGA":"R",
    "AGA":"R",
    "GGA":"G",
    "TGG":"W",
    "CGG":"R",
    "AGG":"R",
    "GGG":"G"
}

"""
FindCodon receives a sequence and the sequence of codon and searches for the codon
alont the sequence returning a list with the starting positions of the codon
of interest
"""
def FindCodon(sequence, codon_sequence):
    codon_positions = []

    for nt in range(0, len(sequence)):

        if sequence[nt:(nt+3)] == codon_sequence:

            codon_positions.append(nt)

    return codon_positions

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
Translates a sequence of codons into aminoacids
"""
def TranslateSequence(codon_sequence):
    aa_string = ""
    stop = False
    i = 0
    while i < len(codon_sequence) and not stop:
        if codon_sequence[i] not in ["TGA","TAA", "TAG"]:
            aa_string = aa_string + codon_table[codon_sequence[i]]
        else:
            aa_string = aa_string + codon_table[codon_sequence[i]]
            stop = True
        i += 1
    return(aa_string)

"""
returns the reverse complement of a sequence
"""
def ReverseComplement(sequence):
    rev_complement = ""
    for i in reversed(range(0, len(sequence))):
        if sequence[i] == "A":
            rev_complement += "T"
        elif sequence[i] == "C":
            rev_complement += "G"
        elif sequence[i] == "G":
            rev_complement += "C"
        elif sequence[i] == "T":
            rev_complement += "A"
        else:
            print("Error: non canonical nucleotide detected")
    return rev_complement


"""
main
"""

input_filename = './rosalind_orf.txt'

infile = open(input_filename, 'r')

for line in infile:
    if re.match(">", line) is None:
        dna_sequence = line.rstrip()
        comp_dna_sequence = ReverseComplement(dna_sequence)

        start_codons = FindCodon(dna_sequence, "ATG")
        rev_start_codons = FindCodon(comp_dna_sequence, "ATG")

        """
        print the aa for the sense sequence
        """
        for i in start_codons:
            codon_dna = GetCodons(dna_sequence[i:len(dna_sequence)])
            aa = TranslateSequence(codon_dna)
            if re.search("x$", aa) is not None:
                print(aa)

        """
        print the aa for the rev_sequence
        """
        for i in rev_start_codons:
            rev_codon_dna = GetCodons(comp_dna_sequence[i:len(comp_dna_sequence)])
            rev_aa = TranslateSequence(rev_codon_dna)
            if re.search("x$", rev_aa) is not None:
                print(rev_aa)

