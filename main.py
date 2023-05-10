"""This program counts the number of vowels in a string."""
def count_vowels(string:str) -> int:
    num_vowels=0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

