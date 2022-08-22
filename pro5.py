"""
The task you have to perform is “Palindromic the List.”
This task consists of a total of 10 points to evaluate your performance.

Problem Statement:-
You are given a list that contains some numbers.
You have to print a list of the next palindromes only if the number is greater than 10;
otherwise, you will print that number.

Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]
"""


def next_palindrome(num):
    num += 1
    while not is_palindrome(num):
        num += 1
    return num


def is_palindrome(num):
    return str(num) == str(num)[::-1]


if __name__ == '__main__':
    n = int(input("Enter your numbers length : "))
    mylist = []
    palindrome_list = []
    for i in range(n):
        list_item = int(input(f"Enter your {i + 1} number"))
        mylist.append(list_item)

    for i in mylist:
        if i > 10:
            palindrome_list.append(next_palindrome(i))
        else:
            palindrome_list.append(i)

    print(palindrome_list)