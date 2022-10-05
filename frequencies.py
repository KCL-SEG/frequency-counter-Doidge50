"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(*args):

    args_list =[]
    for item in args:
        args_list.append(item)

    frequencies = {}
    for item in args_list:
        frequencies.update({item : args_list.count(item)})
    
    return frequencies

print(frequencies(1,2,4,5,"hello",1,1,"hello"))
