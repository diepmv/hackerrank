'''
problem:
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

+Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

+Input Format

The first line contains an integer, N, the number of students. 
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

'''

def find_second_lowest(lst):
    first = lst[0][0]
    for index, val in enumerate(lst):
        if val[0] != first:
            return index
        
def find_second_lowest_list(index, lst):
    result = [lst[index][1]]
    for val in lst[index+1:]:
        if val[0] == lst[index][0]:
            result.append(val[1])
        else:
            break
    result.sort()
    return result

if __name__ == '__main__':
    lst = list()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([score, name])
    lst.sort()
    
    second_lowest = find_second_lowest(lst)
    second_lowest_list = find_second_lowest_list(second_lowest, lst)
    for i in second_lowest_list:
        print(i)
