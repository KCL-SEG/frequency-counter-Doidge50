"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):


    frequencies = {}
    for i in items:
        frequencies.update({i : items.count(i)})
    
    return frequencies

print(frequencies(1,2,4,5,"hello",1,1,"hello"))
