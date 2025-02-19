def swap_case(s):
    word = ''
    for abc in s:
        if abc.isupper():
            word += abc.lower()
        
        elif abc.islower():
            word += abc.upper()
        
        else:
            word += abc
            
    return word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)