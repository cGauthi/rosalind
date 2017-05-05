#!/usr/bin/env python3

infile = open("/home/cgauthi/Dropbox/Programming/Rosalind/q5_GC/rosalind_gc.txt")

def gcc(infile):
    topseq_name = ""
    topseq_gc = 0
    seq_name = ""
    seq = ""
    
    for line in infile:
        if line.startswith(">"):
            if (len(seq) > 0):
                gc_count = 0
                for base in seq:
                    if (base == "C" or base == "G"):
                        gc_count += 1
                gc_rat = gc_count / len(seq)

                if (gc_rat > topseq_gc):
                    topseq_name = seq_name
                    topseq_gc = gc_rat

            seq_name = line.rstrip()[1:]
            seq = ""
        else:
            seq = seq + line.rstrip()

    gc_count = 0;
    for base in seq:
        if (base == "C" or base == "G"):
            gc_count += 1
        gc_rat = gc_count / len(seq)

        if (gc_rat > topseq_gc):
            topseq_name = seq_name
            topseq_gc = gc_rat
    
    print(topseq_name)
    print(topseq_gc*100)

gcc(infile)
