# STRINGS - Exercises

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

# ----------------------------------------------


# DICTIONARIES - Exercises
# Ordered, changeable, Does not allow duplicates

# Creating, Accessing, Changing and Adding, Removing elements, dict comprehension
# membership testing, iterating through dict, and some built-in functions

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

def print_squares():
    # use dictionary comprehension to count express 15 key:value pairs

    # this is equivalent of
    squares = {x: x*x for x in range(15)}
    print(squares)

    # this.
    squares_2 = {}
    for x_ in range (15):
        squares_2[x_] = x_*x_
   #print(squares_2)

def sort_by_key():
    dict1 = {5: 10, 3: 20, 2: 30, 1: 40, 4: 50}

    for keys_, values_ in sorted(dict1.items()):
        print(keys_)

def get_max_min():
    dict1 = {5: 10, 3: 20, 2: 30, 1: 40, 4: 50}

    # lambda is an anonymous function. Can take any num of arguments
    # but can have only one expression: -> lambda arguments : expression
    MAX_VAL = max(dict1.keys(), key=(lambda k: dict1[k]))
    MIN_VAL = min(dict1.keys(), key=(lambda k: dict1[k]))

    print("max: ", dict1[MAX_VAL])
    print("min: ", dict1[MIN_VAL])

def clear_list():

    orig = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

    for keys, values in orig.items():
        values.clear()

    print(orig)


# TUPLES

def unpack_tuple():
    tuplex = (4,8,3)
    n1,n2,n3 = tuplex
    #unpack a tuple in variables
    print(n1 + n2 + n3)
    #not enough values to unpack
    #n1,n2,n3,n4=tuplex

def add_item_t():
    # tuples are immutable, so you cannot add new elements
    # using merge of tuples with + operator, you can add new elements and
    # it will create a new tuple

    tuplex = (4,6,3,23,6)
    tuplex = tuplex +(9,5)
    tuplex = tuplex + ("deniz", "yaman")
    print(tuplex)

def convert_t():

    tuplex = (1,2,["yaman","deniz"])
    tuplex_str = str(tuplex)
    #print(tuplex_str)
    print(type(tuplex_str))

    tup = ('e','x', 'e','1','2')
    new_str = ''.join(tup)
    print(new_str)

def find_repeating():

    tuplex = (1,2,2,2,3,3,3,4)
    count = tuplex.count(2)
    print(count)

def remove_empty_tuples():
    sample = [(),(),('',), ('a','b')]

    sample = [x for x in sample if x]
    print(sample)




if __name__ == '__main__':
    #print(ex1('abc', 'xyz'))
    #print(ex2('deniz'))
    #ex3(500000,50000)
    #dict_example1()
    #dict_concat()
    dict1 = {1: "apples", 2: "bananas"}
    dict2 = {3: "man", 4: "woman"}
    #print(dict_concat_using_pipe(dict1, dict2))
    #is_present(5)
    #iterate_dict()
    #print_squares()
    #sort_by_key()
    #get_max_min()
    #clear_list()


    my_tuple = (1, 2, "deniz")
    print(my_tuple)
    tuple_numbers = (1,2,3)
    tuple_numbers = 1,
    print(tuple_numbers)
    unpack_tuple()
    add_item_t()
    convert_t()
    find_repeating()
    remove_empty_tuples()



