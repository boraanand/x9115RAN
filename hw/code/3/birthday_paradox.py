"""
The (so-called) Birthday Paradox:
   1. Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.
   2. If there are 23 students in your class, what are the chances that two of you have the same birthday? You can estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can generate random birthdays with the randint function in the random module.
"""
from __future__ import print_function, division
from collections import defaultdict

def has_duplicates(l):
    """
    A function to determine if a list contains duplicates
    l: list
    """
    count_dict = defaultdict(int)
    for x in l:
        count_dict[x] += 1
        if count_dict[x] > 1:
            return True
    return False

def same_birthday():
    import random
    random.seed(245)

    #Run the experiment 100 times
    result = []

    for i in range(100):
        sample = [random.randint(1, 365) for x in range(23)]
        
        if has_duplicates(sample): result.append(1)
        else: result.append(0)
    probability = sum(result)/100
    return probability


