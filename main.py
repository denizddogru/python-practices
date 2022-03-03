# Intermediate, python exercises.


'''

welcome

double shift -> search everywhere
control + r -> run boi

'''

import pdb

def str_finder():
    # want to count the occurrences of substring "rr" or any without using the same occurence (non-occurring elements)
    # we need to implement the count function.

    str = "babbababaaaabbbabbabbbabbabbaabbabbababbabbabba"
    str2 = "babba"
    count = 0

    str_len = len(str)
    str2_len = len(str2)

    if str2_len > str_len:
        return count

    i = 0
    while i < str_len:
        if  str2  in str[i: i + str2_len]:
            count += 1
            i = i + str2_len
        else:
            i += 1
    return count



def example3(main_str, sub_str):

    # same as the example below, but now the substrings are converted into numbers and we count them inside the main string
    # then we print the updated string.

    LEN_MAIN = len(main_str)
    LEN_SUB = len(sub_str)

    # xxyyyyy
    # yy
    counter = 0
    i=0
    # pdf.set_trace() is a breakpoint which tells that when the program runs it will start executing from that line in the debugging mode

    pdb.set_trace()
    while i < LEN_MAIN:
        if main_str[i: i+LEN_SUB] == sub_str:
            counter += 1
            main_str = main_str[0:i] + str(counter) +  main_str[i+LEN_SUB : LEN_MAIN]
            LEN_MAIN = len(main_str)
        else:
            i += 1

    return main_str






if __name__ == '__main__':

    # Pythonda debugging çalış
    # aynı soruyu başka bi yöntemle daha çöz

     x = example3("dendendendendendendendendendendendendendendendendendendenden", "den")
     y = example3("rrrrrrrrrrrrrrrrrrrr", "r")
     print(x)
     print(y)





