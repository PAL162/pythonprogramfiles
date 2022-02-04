'''You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
Sample Input: HackerRank.com presents "Pythonist 2".
Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".'''

def swap_case(s):
    x = ""
    for let in s:
        if let.isupper() == True:
            x += (let.lower())
        else:
            x += (let.upper())
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
#Khant Pal_D21CE162