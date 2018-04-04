'''
problem:
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

ref: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
'''


def generate_row(size, row):
    if row - size >=0:
        row = 2*size - row -2
    width = size*4 - 3
    center_element = chr(97+size-row-1)
    lst = [center_element]
    for i in range(97+size-row,97+size):
        lst.insert(0, chr(i))
        lst.append(chr(i))
    row = '-'.join(lst)
    row = row.center(width, '-')
    return row
        
def print_rangoli(size):
    # your code goes here
    width = size*4 - 3
    high = size*2 - 1
    for i in range(high):
        print(generate_row(size, i))
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
