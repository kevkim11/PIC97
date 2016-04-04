def compare(a, b):
    """
    :param a: int or string
    :param b: int or string
    :return: Using an if construct, write a function compare that accepts two numerical or string arguments
            a and b and returns 1 if a is greater than b, 0 if a equals b, -1 if b is greater than a.
    """
    if(a>b):
        return 1
    elif(a==b):
        return 0
    else:
        return-1

def num_squared_print(num):
    """
    :param num:
    :return: Write a for loop to print out the squares of integers 1 through 10 like 1 squared is 1, 2
            squared is 4, 3 squared is 9, etc...
    """
    for i in range(1, num+1):
        squared = i**2
        print i," squared is ",squared
def range_list(start, stop, step):
    """
    :return: Pass the appropriate arguments to the range function such that it returns the list [6, 3, 0, -3, -6]
    """
    l = []
    for i in range(start, stop, step):
        l.append(i)
    return l

def count_arg(*arg):
    """
    :return: Write a function count_args that accepts any number of input arguments and returns the number of arguments it received, e.g. count_args(10,2,3,1) returns 4 and count_args([10,2,3,1]) returns 1.
    """
    return len(arg)

def my_fun(a = 10, b = 20):
    """
    Predict the output of the following:
    my_fun() 10 20
    my_fun(1) 1 20
    my_fun(1,2) 1 2
    my_fun(b=30) 10 30
    """
    print a, b

"""
Given the following:
months_tuple = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
Write a lambda function num_to_month that converts an integer into the name of the month of the year, e.g. num_to_month (2) returns February (not March). T
"""
months_tuple = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
num_to_month = lambda x:months_tuple[x-1]

