#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 13

# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def longest_substring(s,k):

    cache = [None for _ in range(k)]
    current_substring = ""
    count = 0
    max_count = 0
    
    while len(s) > 0:
        chr = s[0]
        s = s[1:]
        current_substring +=chr

        if chr in cache: # cache stores the list of distinct characters, with most recent being last
            count+=1
            cache += [cache.pop(cache.index(chr))]

        else: # if character is not in the cache...

            if None in cache: # character is added if there's a blank space in the cache
                cache.pop(cache.index(None))
                cache += [chr]
                count+=1
                
            else: # oldest char is removed from cache, max_count is updated if necessary, and substring before old char is removed
                old_chr = cache.pop(0)
                cache += [chr]

                if max_count < count:
                    max_count = count
                    
                idx = len(current_substring) - current_substring[::-1].index(old_chr) - 1
                current_substring = current_substring[idx+1:]
                    
                count = len(current_substring)

    # final max count check 
    if max_count < count:
                max_count = count
    return max_count
        

# TEST CODE:
k = 2
s = "abcba"

assert longest_substring(s,k) == 3