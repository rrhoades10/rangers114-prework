# Question 1 - Write a function to print "Hello USERNAME"
def say_hello(elephants):
    print(f"Hello {elephants}!")


say_hello("Your mom")


# def hello_name(username):
#     print("Hello, " + username.title() + "!")


# hello_name('ampowers')


# def get_user(username):
#  print("Hello, " + username.title() + "!")


# get_user("dharti")


# def hello_name(user_name):
#     """a function to print hello_USERNAME
#     this is abunch of stuff that doesnt matter
#     but pretend is extensive instructions on
#     how the code works"""
#     print("hello, " + user_name.title()+"!")


# """Let's call "hello_name" function"""
# hello_name("john")

# comment out code here and it wont interfere with anything else
# sdfsdfsdfsdf


# Question 2 - Print first odd numbers between 1 and 100
def first_odds():
    """Print all odd numbers from 1 to 100."""
    for number in range(1, 101):
        if number % 2 == 0:
            continue
        else:
            print(number)


first_odds()


def first_odds():
    """Print the odd numbers from 1 - 100"""
    number = 1
    while number < 101:
        if number % 2 == 1:
            print(number)
            number += 1
        else:
            number += 1


def odd_number():
    num = list(range(1, 101))
    for no in num:
        if no % 2 != 0:
            print(no)


odd_number()


print("Odd numbers 1 - 100:")
for x in range(1, 100+1):
    if x % 2 == 1:
        print(x)


def first_odds():
    # my code
    for num in range(1, 101, 2):
        print(num)
# You can call this function simply by typing first_odds()
# first_odds()


def first_odds():
    """a function that prints the odd numbers from 1-100 and returns nothing"""
    # num = 1
    for num in range(100):

        if num % 2 == 1:  # num%2!=0 will get the same result
            print(num)


first_odds()

# Question 3 - Write a function that returns the max number in a given list

a_list = [5, 101, 110, 20, 105, 300, 17, 250, 75]


def max_num_in_list(a_list):
    """ a function to find the maximum number in a list"""
    maximum = max(
        a_list)  # this function would still work without the variable declaration
    print("The Maximum number in a_list is ", maximum)


max_num_in_list(a_list)


def max_num_in_list(a_list):
    print(max(a_list))


my_list = [1, 3, 53, 6, 7, 4, 24]
max_num_in_list(my_list)


def max_num_in_list2(a_list):
    a_list.sort()
    return a_list[-1]


max_num_in_list2([1, 3, 53, 6, 7, 4, 24])


def max_num_in_list(a_list):
    '''For any given list argument containing only numbers,
 this returns the max number in that list'''
    return sorted(a_list, reverse=True)[0]

# code to get maxmimum number among list


def max_number_in_list(a_list):
    max_number = max(a_list)
    return max_number


test = max_number_in_list([4, 5, 20, 8, 10])
print(test)


def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max


print(max_num_in_list([-5, 0, 5, 10]))


# Question 4 - Write a function to return of the given year is a leap year.
def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(str(a_year) + " is a leap year")
    else:
        print(str(a_year) + " is not leap year")


is_leap_year(2020)
is_leap_year(2019)


def is_leap_year(a_year):
    """ a function to return if the given year is a leap year """
    if a_year % 400 == 0 and a_year % 100 == 0:
        print(a_year, "is a leap year")
    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif a_year % 4 == 0 and a_year % 100 != 0:
        print(a_year, "is a leap year")
    else:
        print(a_year, "is not a leap year")


is_leap_year(2000)


def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
        return True
    else:
        return False


# Question 5 - Write a function to check if all numbesr in a list are consecutive
def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
    print(status)


# is_consecutive([1, 3, 4, 5, 6, 7, 8, 9])


def is_consecutive(a_list):
    '''This function takes a list of numbers, and returns True if all
 numbers in the list are one up or one down from the number right before.
  If any two numbers next to each other on the list are more than 1 apart
  in value, the program returns False.'''
    next_num_val = -1
    for index, sel_num_val in enumerate(a_list):
        # If index of currently-selected number in list is less than
        # index of last number on list, grab the value of following num.
        if index < len(a_list)-1:
            next_num_val = a_list[index+1]
        else:
            # If index reaches last number on list, it found no non-
            # consec numbers and will exit, returning True.
            return True
        # print(index,sel_num_val, next_num_val) # This line for testing
        if sel_num_val - next_num_val == 1 or sel_num_val - next_num_val == -1:
            continue
        else:
            return False


print(is_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9]))

my_list = [2, 5, 3, 6, 8, 10]


def is_consecutive(a_list):
    sorted_list = a_list[:]
    sorted_list.sort()
    compare_list = [sorted_list[0]]
    for num in range(sorted_list[0], len(sorted_list)):
        compare_list.append(num+1)
    if compare_list == sorted_list:
        return True
    else:
        return False
