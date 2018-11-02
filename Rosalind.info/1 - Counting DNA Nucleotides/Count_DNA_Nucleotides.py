'''
Usage: Count_DNA_Nucleotides.py data.txt
'''


import sys
from collections import defaultdict


# datafile = sys.argv[1]

# with open(datafile, "r") as data:
    # data = "".join(data.readlines())
    # data_items = data


data_items = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
def count(data_items):
    count = defaultdict(int)
    for i in data_items:
        count[i] += 1
    return count

count = count(data_items)

for i in count:
    print(i, ": ", count[i], sep="")

print("A", " C", " G", " T")
print(count["A"], count["C"], count["G"], count["T"])
