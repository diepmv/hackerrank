''''
problem:
You are given a string S and width w. 
Your task is to wrap the string into a paragraph of width w.

Input Format

The first line contains a string, S. 
The second line contains the width, w.

a, b = raw_input(), int(raw_input())

for i in range(0,len(a),b):

print a[i:i+b]
''''


import textwrap

def wrap(string, max_width):
    index = 0
    new_string = ''
    while index <= len(string):
        new_string = new_string + string[index: index+max_width] +'\n'
        index += max_width
    return new_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
