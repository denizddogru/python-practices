# Strings
def ex1(a, b):
    new_a = b[:2] + a[2:]  # ab+z
    new_b = a[:2] + b[2:]  # xy+c

    return new_a + ' ' + new_b


def ex2(a):
    new_string = a[2:]  # niz

    return new_string

# display a  number with a comma seperator
# 50000
def ex3(a,b):

    print("Number with comma seperator: "+"{:,}".format(a));
    print("Number with comma seperator: " + "{:,}".format(b));



# DICTIONARIES
# Ordered, changeable, Does not allow duplicates

def dict_example1():
    # my_dict = dict({1: "apple", 2: "banana"})
    my_dict =  {0: 10, 1: 20}
    print(my_dict)

    # add element to the ent of the list
    my_dict[2] = 30
    print(my_dict)


def dict_concat():
    dic1 = {1:10, 2:20}
    dic2 = {3:30, 4:40}

    return (dic1.update(dic2))

def dict_concat_using_pipe(dict1, dict2):

    result = dict1 | dict2
    return result

def is_present(x):
    dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    if x in dict1:
        print("Key is present.")
    else:
        print("Key is not found.")

def iterate_dict():
    dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    for dict_key, dict_value in dict1.items():
        print(dict_key, '->', dict_value)








if __name__ == '__main__':
    #ex3(500000,50000)
    #dict_example1()
    #dict_concat()

    dict1 = {1: "apples", 2: "bananas"}
    dict2 = {3: "man", 4: "woman"}
    #print(dict_concat_using_pipe(dict1, dict2))

    #is_present(5)
    #iterate_dict()


# print(ex1('abc', 'xyz'))
# print(ex2('deniz'))

# print("Hello World")s
