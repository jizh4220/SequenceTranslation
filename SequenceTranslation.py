#!/usr/bin/env python
import sys

def read_seq(filepath):
    try:
        with open(filepath, "r") as file:
            std = ["A","T","C","G"]
            seq = file.read()
            seq = seq.replace("\n", "")
            seq = seq.replace("\r", "")
            seq = seq.upper()
            
            if any(flag not in std for flag in seq): #early terminate with none DNA sequence
                print('Incorrect sequence')
                return None
            
            return seq
    except IOError:
        print('Cannot find the input file')

def translate(seq):
    print('Input DNA Sequence: ', seq)
    print('\n')
    protein = ""
    start = "ATG"
    stop = ["TAA", "TAG", "TGA"]
    table = {
        "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
        "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
        "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
        "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
        "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
        "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
        "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
        "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
        "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
        "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
        "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
        "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
        "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
        "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
        "TAC": "Y", "TAT": "Y", "TAA": "*", "TAG": "*",
        "TGC": "C", "TGT": "C", "TGA": "*", "TGG": "W"
    }

    for i in range(len(seq)):
        if len(seq)-i < 3:
            print('Cannot find start codon, function terminates')
            return protein
        if seq[i:i+3] == start: #Traverse the entire DNA sequence
            for j in range(i,len(seq),3): #Once start codon is found, translate 3bp at a time
                if len(seq)-j < 3: #Can't find stop codon
                    print('Cannot find stop codon, function terminates')
                    return protein
                codon = seq[j:j+3]
                if codon in stop: 
                    print('Successful translation, Output Amino Acid Sequence: ', protein)
                    return protein
                protein += table[codon]




def main(filepath):
    seq = read_seq(filepath)
    if seq:
        protein = translate(seq)
        return protein
    #print('Unknown input sequence')

if __name__ == '__main__':
    main(sys.argv[1])   
