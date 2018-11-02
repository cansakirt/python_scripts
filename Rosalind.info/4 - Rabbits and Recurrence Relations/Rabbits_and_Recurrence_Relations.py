'''
Usage: Rabbits_and_Recurrence_Relations.py data.txt
'''
i = 0

def rabbits(n, k):
    global i
    # print("-------")
    if n == 0:
        # print("returned 0")
        return 0
    if n == 1:
        # print("returned 1")
        return 1
    else:
        # print("returning more for", n-1, "and", n-2)
        i += 1
        return rabbits(n-1, k) + k*rabbits(n-2, k)

print(rabbits(32,3), i, sep="\n")