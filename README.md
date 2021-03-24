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
If the file format is correct regardless of lowercase and uppercase 
If start and stop codons successfully found:
```
Successful translation, Output Amino Acid Sequence:  MKKMQSIVLALSLVLVAPMAAQAAEITLVPSVKLQIGDRDNRGYYWDGGHWRDHGWWKQHYEWRGNRWHPHGPPPPPRHHKKAPHDHHGGHGPGKHHR
```
