'''
problem:

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.
'''

def capitalize_word(word):
    lst = list(word)
    lst[0] = lst[0].upper()
    return ''.join(lst)

def capitalize(string):
    lst = string.split()
    return ' '.join(list(map(capitalize_word, lst)))


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
