
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


def main():
    """
      -- Basic Python Exercises part2 from the site below --
      https://www.w3resource.com/python-exercises/basic/
    """
    print(is_different([1,5,7,9]))
    print(is_different([1,2,3,3,4,5,6]))





if __name__ == '__main__':
    main()
