"""
the idea is to find the total count of sub_string in string

ABCDCDC - string(s)
CDC - sub_string(ss)

string -> len = 7
sub_string -> len = 3

7-3+1 = 5(loop)
i = range(0,5)

s[i:i+3] == ss

i=0
s[0:3] == ss
ABC == CDC

i=1
s[1:4] == ss
BCD == CDC

i=2, count = 1
s[2:5] == ss
CDC == CDC

i=3
s[3:6] == ss
DCD == CDC

i=4, count = 2
s[4:7] == ss
CDC == CDC


"""


def count_substring(string, sub_string):
    # total count of sub_string in string
    count = 0

    # find the len of sub_string and string
    len_string = len(string)
    len_sub_string = len(sub_string)
    
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)