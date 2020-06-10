#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 2

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?


# A simple solution

def simple_sum_arr( lst ): # solve by dividing the product of the array by each element

    output=[]
    total=1

    for num in lst: # a loop to calculate the total product of the the array
        if num==0:
            return("this method doesn't support 0 in array")
        total=total*num
    
    for num in lst: # divide the product by each element of the array
        output+=[total/num]

    return output

# A solution to the no division follow up

def no_division_sum_arr( lst ): 

    output=[]

    for num in lst:
        total=1

        for num in lst[1:]:   # each number in the list--except for the first--is mulitplied with every other
            total*=num  
        output.append(total) # total added to the output 
        lst.append(lst.pop(0)) # number at the start of array moved to the end

    return output


# TEST CASES
lst=[1, 2, 3, 4, 5]
print(simple_sum_arr(lst))
print(no_division_sum_arr(lst))

lst=[3,2,1]
print(simple_sum_arr(lst))
print(no_division_sum_arr(lst))

lst=[5,10,0] # Here, we see why avoiding division may be preferred, as the simple solution won't compute
print(simple_sum_arr(lst))
print(no_division_sum_arr(lst))

lst=[2] # will always merely ouput a '1'. It's not clear what the expected value should be. Perhaps 0?
print(simple_sum_arr(lst))
print(no_division_sum_arr(lst))
