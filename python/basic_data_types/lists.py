"""
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, n, denoting the number of commands. 
Each line i of the n subsequent lines contains one of the commands described above.

+Constraints

The elements added to the list must be integers.
+Output Format

For each command of type print, print the list on a new line.

def get_operation(input):
    lst = input.split(' ')    
    operation = lst[0]
    if len(lst) == 2:
        args = [int(lst[1])]
    elif len(lst) == 3:
        args = [int(lst[1]), int(lst[2])]
    else:
        args = []
    return operation, args
    
if __name__ == '__main__':
    L = []
    N = int(input())
    for i in range(N):
        a = input()
        operation, args = get_operation(a)
        if len(args)==0 and operation != 'print':
            b = getattr(L, operation)
            b()
        elif len(args)==1:
            try:
                b = getattr(L, operation)
                b(args[0])
            except:
                pass
        elif len(args)==2:
            b = getattr(L, operation)
            b(int(args[0]), int(args[1]))
        else:
            print(L) 

"""
n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print l        
