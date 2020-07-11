# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 33

# This problem was asked by Microsoft.

# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

def median(seq):
    sorted_seq = []

    while len(seq) > 0:

        val = seq.pop(0)

        if len(sorted_seq) == 0:
            sorted_seq.append(val)
            print(val)

        elif len(sorted_seq) == 1:
            if sorted_seq[0] < val:
                sorted_seq += [val]
            else:
                sorted_seq = [val]+sorted_seq
            print(float(sorted_seq[0]+sorted_seq[1])/2)

        else:
            mid_val = len(sorted_seq) // 2
            while val != None:
                
                if mid_val == 0:
                    sorted_seq = [val]+sorted_seq
                    val = None

                elif mid_val+1 == len(sorted_seq):
                    sorted_seq += [val]
                    val = None

                elif val < sorted_seq[mid_val]:
                
                    if val > sorted_seq[mid_val-1]:
                        sorted_seq = sorted_seq[:mid_val]+[val]+sorted_seq[mid_val:]
                        val = None

                    else:
                        mid_val = mid_val // 2

                else:
                    if val < sorted_seq[mid_val+1]:
                        sorted_seq = sorted_seq[:mid_val+1]+[val]+sorted_seq[mid_val+1:]
                        val = None
                    else:
                        mid_val = (len(sorted_seq) + mid_val) // 2
            
            length = len(sorted_seq)
            if length % 2 == 0:
                middle = length // 2
                median = float(sorted_seq[middle-1]+sorted_seq[middle])/2
            else:
                median = sorted_seq[length//2]
            print(median)
    
median([2, 1, 5, 7, 2, 0, 5])