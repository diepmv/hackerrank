"""
problem:
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""

def swap_case(s):
    new_str = ""
    for _ in s:
        if _.islower():
            new_str += _.upper()
        else:
            new_str += _.lower()
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
