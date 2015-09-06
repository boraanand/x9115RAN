from ok import *
from birthday_paradox import * 

@ok
def _has_duplicates_1():
    with_duplicates = [1, 2, 2, 3, 4]
    assert has_duplicates(with_duplicates)

@ok
def _has_duplicates_2():
    without_duplicate = [1, 2, 3, 4]
    assert not has_duplicates(without_duplicate)

@ok
def _same_birthday():
    print(same_birthday())

@ok
def score():
    print(unittest.score())
