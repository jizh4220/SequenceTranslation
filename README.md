# Sequence Translation
Example: 
Input DNA Sequence in a file `text.txt`:  
```
atgaaaaagatgcaatctatcgtactcgcactttccctggttctggtcgctcccatggcagcacaggctgcggaaattacgttagtcccgtcagtaaaattacagataggcgatcgtgataatcgtggctattactgggatggaggtcactggcgcgaccacggctggtggaaacaacattatgaatggcgaggcaatcgctggcacccacacggaccgccgccaccgccgcgccaccataagaaagctcctcatgatcatcacggcggtcatggtccaggcaaacatcaccgctaa
```
Run SequenceTranslation with an input DNA sequence file
```
python3 SequenceTranslation.py text.txt
```
If the file format is correct with only "A","T","C","G", regardless of lowercase and uppercase, the algorithm prints the input sequence in all uppercase
```
Input DNA Sequence: ATGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCAGCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGATAATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACATTATGAATGGCGAGGCAATCGCTGGCACCCACACGGACCGCCGCCACCGCCGCGCCACCATAAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA
```
If start and stop codons successfully found:
```
Successful translation, Output Amino Acid Sequence:  MKKMQSIVLALSLVLVAPMAAQAAEITLVPSVKLQIGDRDNRGYYWDGGHWRDHGWWKQHYEWRGNRWHPHGPPPPPRHHKKAPHDHHGGHGPGKHHR
```
