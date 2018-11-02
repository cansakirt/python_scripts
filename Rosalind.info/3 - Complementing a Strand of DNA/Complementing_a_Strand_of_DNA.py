'''
Usage: Complementing_a_Strand_of_DNA.py data.txt
'''


import sys


datafile = sys.argv[1]

with open(datafile, "r") as data:
    data = "".join(data.readlines())
    data_items = data


# data_items = "AAAACCCGGT"
new_data = list()

for i in data_items:
    if i == "A": 
        i = "T"
    elif i == "T": 
        i = "A"
    elif i == "C": 
        i = "G"
    elif i == "G": 
        i = "C"
    new_data.append(i)

new_data = "".join(new_data[::-1])

print(new_data)

with open("output_file.txt", "w") as output_file:
    # output_file.write(new_data)
    print(new_data, file=output_file)
