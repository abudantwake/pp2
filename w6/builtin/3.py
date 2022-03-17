def rev(string):
    s1 = reversed(string)
    return 'Palindrome' if list(s1) == list(string) else 'Not palindrome'

string = input()
print(rev(string))