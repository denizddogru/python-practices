def is_different(data):
    """"
    1. Write a Python function that takes a sequence
     of numbers and determines whether
    all the numbers are different from each other
    """

    if len(data) == len(set(data)):
        return True
    else:
        return False;


# LIST EXERCISES


def list_(x):
    new_list = [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 9]
    LEN_NEW_LIST = len(new_list)
    new_list_2 = [1, 15, ["apples", 5], ["bananas", 3]]
    result = 0

    dup_items = set()
    unique_list = []

    if not unique_list:
        print("list is empty")


def second_largest(numbers):
    if (len(numbers) < 2):
        return
    if (len(numbers) == 2) and (numbers[0] == numbers[1]):
        return

    dup_items = set()
    uniq_items = []

    for x in numbers:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
        uniq_items.sort()
    return uniq_items[-2]

    print(numbers)

def concat_list_string(some_list):

  result = ''

  for element in some_list:
      result += str(element)
  return result




def main():
    """
      -- Basic Python Exercises part2 from the site below --
      https://www.w3resource.com/python-exercises/basic/
    """


    print(concat_list_string([1,2,3,4,5]))
    second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2])
    print(is_different([1, 5, 7, 9]))
    print(is_different([1, 2, 3, 3, 4, 5, 6]))
    x = []
    list_(x)


if __name__ == '__main__':
    main()
