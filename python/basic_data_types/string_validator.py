"""
problem:
You are given a string S. 
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string S.

Output Format

In the first line, print True if S has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if S has any alphabetical characters. Otherwise, print False. 
In the third line, print True if S has any digits. Otherwise, print False. 
In the fourth line, print True if S has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.


"""

#First solution
def is_contain_x(s, valid_method):
    for _ in s:
        string_method = '"{0}".{1}()'.format(_, valid_method)
        if eval(string_method):
            return True
    return False

if __name__ == '__main__':
    s = input()
    print(is_contain_x(s, 'isalnum'))
    print(is_contain_x(s, 'isalpha'))
    print(is_contain_x(s, 'isdigit'))
    print(is_contain_x(s, 'islower'))
    print(is_contain_x(s, 'isupper'))


#Second solution
str = raw_input()
print any(c.isalnum()  for c in str)
print any(c.isalpha() for c in str)
print any(c.isdigit() for c in str)
print any(c.islower() for c in str)
print any(c.isupper() for c in str)
