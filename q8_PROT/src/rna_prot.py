#!/usr/bin/env python3

aa_table = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'UCU':'S', 'UCC':'S',
        'UCA':'S', 'UCG':'S', 'UAU':'Y', 'UAC':'Y', 'UAA':'', 'UAG':'',
        'UGU':'C', 'UGC':'C', 'UGA':'', 'UGG':'W', 'CUU':'L', 'CUC':'L',
        'CUA':'L', 'CUG':'L', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
        'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q', 'CGU':'R', 'CGC':'R',
        'CGA':'R', 'CGG':'R', 'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
        'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'AAU':'N', 'AAC':'N',
        'AAA':'K', 'AAG':'K', 'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
        'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V', 'GCU':'A', 'GCC':'A',
        'GCA':'A', 'GCG':'A', 'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E', 'GGU':'G',
        'GGC':'G', 'GGA':'G', 'GGG':'G'}

infile = open("../data/rosalind_prot.txt")

def rnatrans(infile):
    seq = str(infile.read())
    codon = ''
    prot_string = ''
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        for k, v in aa_table.items():
            if codon == k:
                if v == "Stop":
                    break
                else:
                    prot_string = prot_string + v
    
    outfile = open('../data/output.txt', 'w+')
    outfile.write(prot_string)
    print(prot_string)

rnatrans(infile)
