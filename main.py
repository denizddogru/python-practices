# Intermediate, python exercises.


'''

welcome

double shift -> search everywhere
control + r -> run boi



    while i < LEN_MAIN:
        if main_str[i: i + LEN_SUB] == sub_str:
            counter += 1
            main_str = main_str[0:i] + str(counter) + main_str[i + LEN_SUB: LEN_MAIN]
            LEN_MAIN = len(main_str)
        else:
            i += 1

    return main_str


'''



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


    while i < LEN_MAIN:
        if main_str[i: i+LEN_SUB] == sub_str:
            counter += 1
            main_str = main_str[0:i] + str(counter) +  main_str[i+LEN_SUB : LEN_MAIN]
            LEN_MAIN = len(main_str)
        else:
            i += 1

    return main_str



def example_4(main_str,sub_str):

    new_list = list(main_str)
    new_sub = list(sub_str)

    LEN_MAIN = len(new_list)
    LEN_SUB = len(sub_str)

    i=0
    counter = 0
    counter_list = []


    # 'x','x','y','y','y'

    while i < LEN_MAIN:
        if new_list[i: i+LEN_SUB] == new_sub:
            counter += 1
            counter_list.append(counter)
            new_list = new_list[0:i] + counter_list + new_list[i+ LEN_SUB: LEN_MAIN]
            LEN_MAIN = len(new_list)
        else:
             i += 1

    return new_list












if __name__ == '__main__':

    # Pythonda debugging çalış
    # aynı soruyu başka bi yöntemle daha çöz




     x = example3("dendendendendendendendendendendendendendendendendendendenden", "den")
     y = example3("rrrrrrrrrrrrrrrrrrrr", "r")

     #import pdb; pdb.set_trace()
     z = example_4(['x','x','x','y','y','x','y'], ['x','y'])
     print(x)
     print(y)
     print(z)






