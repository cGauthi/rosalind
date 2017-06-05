#!/usr/bin/env python3

infile = open("../data/rosalind_cons.txt")
dna_mtx = []
dna = ''

def consensus(fastafile):
    strand = 'NONE'
    for line in fastafile:
        if line.startswith(">"):
            if strand != "NONE":
                dna_mtx.append(strand)
            strand = ''
        else:
            dna = line.rstrip("\n")
            strand = strand + dna

    dna_mtx.append(strand)

    cons_mtx = [[0]*len(strand) for _ in range(4)]

    for row in range(len(dna_mtx)):
        dna = dna_mtx[row]
        for pos in range(len(dna)):
            if dna[pos] == "A":
                cons_mtx[0][pos] += 1
            elif dna[pos] == "T":
                cons_mtx[1][pos] += 1
            elif dna[pos] == "C":
                cons_mtx[2][pos] += 1
            elif dna[pos] == "G":
                cons_mtx[3][pos] += 1

    consensus = ''

    for pos in range(len(dna)):
        base_count = []
        for nt in range(4):
            base_count.append(cons_mtx[nt][pos])

        if base_count[0] == max(base_count):
            consensus = consensus + "A"
        elif base_count[1] == max(base_count):
            consensus = consensus + "T"
        elif base_count[2] == max(base_count):
            consensus = consensus + "C"
        elif base_count[3] == max(base_count):
            consensus = consensus + "G"
    
    print(consensus)
    print("A: " + " ".join(map(str, cons_mtx[0])))
    print("T: " + " ".join(map(str, cons_mtx[1])))
    print("C: " + " ".join(map(str, cons_mtx[2]))) 
    print("G: " + " ".join(map(str, cons_mtx[3])))


consensus(infile)
