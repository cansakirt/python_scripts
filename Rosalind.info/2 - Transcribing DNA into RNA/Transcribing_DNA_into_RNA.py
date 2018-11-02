'''
Usage: Transcribing_DNA_into_RNA.py data.txt
'''

import sys


datafile = sys.argv[1]

with open(datafile, "r") as data:
    data = "".join(data.readlines())
    data_items = data


# data_items = "GATGGAACTTGACTACGTAAATT"


# for i in data_items:
    # i = i.replace("T", "U")
newdata = data_items.replace("T", "U")
print(newdata)

with open("output_file.txt", "w") as output_file:
    # output_file.write(newdata)
    print(newdata, file=output_file)
