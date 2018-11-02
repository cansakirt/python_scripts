'''
Usage: Computing_GC_Content.py data.txt
'''

import sys
from collections import defaultdict


datafile = sys.argv[1]
with open(datafile, "r") as data:
    data = "".join(data.readlines())
    data_items = data


def count_things(data_items):
    count = defaultdict(int)
    for i in data_items:
        count[i] += 1
    return count


def get_sums(count):
    gc_sum = list()
    all_sum = list()
    all_sum.append(count["A"])
    all_sum.append(count["C"])
    all_sum.append(count["G"])
    all_sum.append(count["T"])
    gc_sum.append(count["G"])
    gc_sum.append(count["C"])
    return sum(gc_sum), sum(all_sum)


def calc_rate(tuple):
    gc_sum, all_sum = tuple
    if all_sum == 0:
        return 0
    return gc_sum / all_sum * 100


def largest_gc_content(lst1, lst3):
    # print(max(lst3))
    return lst1[lst3.index(max(lst3))][1:]


def create_dict(data_items):
    ''' Parse a FASTA file read line by line.
        data_items: FASTA file.readlines()
        Return a dictionary where header as key and value as value.
    '''
    fasta_dict = defaultdict(str)
    data_items = data_items.split("\n")
    for i, item in enumerate(data_items):
        if item.startswith(">"):
            current_header = data_items[i]
        else:
            fasta_dict[current_header] += item
    return fasta_dict


def create_list(data_items):
    ''' Parse a FASTA file read line by line.
        data_items: FASTA file.readlines()
        Return a list where:
            even indexes are headers
            odd  indexes are values
    '''
    new_list = list()
    fasta_dict = create_dict(data_items)
    for i in fasta_dict:
        new_list.append(i)
        new_list.append(fasta_dict[i])
    return new_list


def return_numbers(data_items):
    ''' Take a list where:
            even indexes are headers
            odd  indexes are values
        Return three lists where:
            lst1 is headers
            lst2 is values
            lst3 is GC content rates
    '''
    count = defaultdict(None)
    lst1 = list()
    lst2 = list()
    lst3 = list()
    for i, item in enumerate(data_items):
        if not i % 2:
            count[item] = data_items[i+1]
            lst1.append(item)  # headers
            lst2.append(data_items[i+1])  # values
            lst3.append(calc_rate(get_sums(  # GC content rates
                        count_things(data_items[i+1]))))
    return lst1, lst2, lst3

data_items = create_list(data_items)

lst1, lst2, lst3 = return_numbers(data_items)
# print(lst1, lst2, lst3, sep="\n")
print(largest_gc_content(lst1, lst3), max(lst3), sep="\n")
