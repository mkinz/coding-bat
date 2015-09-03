"""Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'"""

def double_char(str):
    new = ""
    for i in range(len(str)):
        new = new + str[i] + str[i]
    return new