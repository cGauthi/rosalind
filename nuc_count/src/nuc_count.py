#!/usr/bin/env python3

s = "TCACGCCGCGGCAACCACTCGCCCGAAGCTTCACGCCGTTTATGATAGCCTATTTATTCTCGGTGGATTTCTCGGATCACCCAGGTTCACAGCCACTCTATAGATTGTGTCCGCGATACGTCTGGGAACAGCCGTCGATGAACAAGGTCCGTAAATAGTGCAATCTCAGAACTCTACCCCTGTACGAGATCGCATTATCAAGCACACAAAAACACGCATAGCACGACTCCAGTGATGTTAGTGGTAGGTGCCGGGAATGCTAGTTCGCCGTTAGTCACTGGGTGTATCGATAACGTCGCGCTCACTGTGTCCTTTACCACACATTGAAATGTCTACCGGGGAGATGGGCGGACCTCATCGTACCCGGCCACCAATGTACACGTTGTTTAGTATGGGTGGAAAGACTGCGGGGTGGAATCACTGTTGACTAGGGACTTACCGTATCTATCCAGTCCGTATTCTTCTGCTATTAGGGCTTAGCGGGCGTTTTCCTACAGACACGGGGGTTATTTACGGGTGGTACGTGGATCGAGCTAAAGAAAAGATGTTCTATAACCTTATGCGTGTGCCTGTATCGCTAGGACTCTCGATTGAGGTATGCGCCGATTCCATTTTGAATGGTGTCAGGGGCGTAAGGGCCTAACATCATCATTTAAGCGTGCGCTGTATACGACGAGCGAGTTGTCATTAACTCGTTCGCGCTAGTAATCCGCGAGGGGGGCCAACGCCACCAAATAATTGACTGCAATCCTGTTGTCTCGAATCATGCACGCGTATCCACAGGTGCGCGAAATAGTTCGGTGAGGGCAGGTTAGCGTTAGCTATTTTCGGACATGTCCTAGTTAAGA"

a_count = s.count("A")
c_count = s.count("C")
g_count = s.count("G")
t_count = s.count("T")

print("{}  {}  {}  {}".format(a_count, c_count, g_count, t_count))
