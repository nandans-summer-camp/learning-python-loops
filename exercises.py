#
# 1) 
# Write a function "only_adults" that
# takes as input a list of numbers and 
# returns only those numbers >= 18



#
# 2) 
# Write a function "get_only_adults" that
# takes as input a list of numbers and 
# returns only those numbers >= 18
# and removes any None values from the list



#
# 3)
# Write a function "are_all_adults" that
# takes as input a list of numbers
# and returns True if they are all >= 18,
# and returns False otherwise
# Is this a map, filter, or reduce?



#
# 4)
# Write a function "count_nones" that
# takes as input a list of any type of element
# and returns a count of how many of those
# elements are None types.
# Is this a map, filter, or reduce?



#
# 5)
# Write a function "longest_word" that
# takes as input a list of strings
# and returns the longest string in the
# list.
# Hint: you will need to use two "accumulators"



#
# 6)
# Write a function "second_highest_number"
# that takes as input a list of numbers
# and returns the second highest. Assume
# that the numbers will be unique (no duplicates).
#
# NOTE: Only use the operations and functions
# we have learned so far! No cheating!
#
# HINT: You might want to write two functions!



#
# 7)
# Write a function "n_highest_number"
# with two parameters: 
# 1. a list of numbers
# 2. an integer
#
# "n_highest_number" should return the nth 
# highest number in the list, where n is the 
# second parameter of the function. Assume
# that the numbers will be unique (no duplicates).
# Also assume that n <= the number of elements 
# in the list.
#
# NOTE: Only use the operations and functions
# we have learned so far! No cheating!
#
# HINT: Can you reuse anything from the previous
# exercise? That may or may not work, depending
# on how you implemented it. 
#
# HINT HINT: you can use the function "range"
# in the Python documentation: 
# https://docs.python.org/3/library/stdtypes.html#typesseq-range
# to create a list of arbitrary length
#
# HINT HINT HINT: Don't try and be "efficient"!



#
# 7)
# Write a function "every" that
# takes two parameters:
# 1. a list of elements of data type E
# 2. a predicate function (E) -> bool. In
# other words, a function that has a single
# parameter, which is the same type as the
# elements of the list, and returns a boolean.
#
# "every" should return True if the predicate
# evaluates to true for every element in the list.
# Otherwise, it returns False.
#
# NOTE: we haven't yet seen functions
# passed as arguments, so this might  
# feel strange. But it works!
