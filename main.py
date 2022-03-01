# Intermediate, python exercises.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

'''
# 1 Lists: ordered, mutable, allows duplicate elements


'''


def main():
    mylist = ["banana", "cherry", "apple"]
    print(mylist)

    if "banana" in mylist:
        print("yes")
    else:
        print("no")

    mylist.append("lemon")

    mylist.insert(1, "melon")
    print(mylist)

    item = mylist.pop()
    print(item)
    print(mylist)


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

def str_finder_():
    str = "rrrrrrrr"
    str2 = "rrrr"
    count = 0

    str_len = len(str)
    str2_len = len(str2)

    if str_len < str2_len:
        return count
    i=0
    while i < str_len:
        if str_len == 0 or str2_len == 0:
            count = 0
        if str == str2:
            count += 1
        if str[i: i+str2_len] == str2:
            count += 1
            i = i+str2_len
        else:
            i += 1
    return count

def str_finder_2():

















if __name__ == '__main__':
    # main()
    x = str_finder_()
    print(x)
