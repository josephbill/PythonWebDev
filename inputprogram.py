def user_input():
    # infinite loop
    while True:
        user = input("Enter your word: ")
        if user.lower() == "exit":
            break
        print(f"the users input is {user}")


#user_input()

def reverse_list_strings(list_strings):
    list_reverse = [] # initializing an empty list to hold my reversed items
    for i in list_strings:
        print(i)
#         how can you reverse a string (i)
        reversed_string = i[::-1]
        list_reverse.append(reversed_string)
    return list_reverse

#print(reverse_list_strings(["apple","banana","cherry"]))


def print_even_keys(input_dict):
    for key, value in input_dict.items():
        # checking if value is even
        if value % 2 == 0:
            print(f"{key} is even")

    return "Function running"

# print(print_even_keys({'a': 2, 'b': 3, 'c': 4}))


def has_distinct(nums,target):
    """
    in the context of this problem 'distinct' means two different numbers in the list that adds up to the target
    e.g 3 + 5 = 9 , even though they appear multiple times , the functions needs to find one pair
    of distinct numbers that satisfy the condition.

    0. Initialize a data structure(sequences) to track the numbers encountered so far
    1. Iterate through the numbers in the input list 
    2. for each number we calculate the difference needed to reach the target sum 
    3. if the sum difference is not found in seen number : it return TRUE, indicating a pair exists
    4. if no such pair exists , return false , i.e. the sum difference appears more than once
    """
    seen_number = {}
    for num in nums:
        print(f"The number in current iterations is : {num} ")
        sum_difference = target - num
        print(sum_difference)
        if sum_difference in seen_number and seen_number[sum_difference] > 0:
            return True
        seen_number[num] = seen_number.get(num,0) + 1 # counting the occurances of the number in my dictionary
        print(seen_number)
    return False

nums = [10,2,10,3,4,5,5]
sum = 20
result = has_distinct(nums,sum)
print(f"Are there two distinct numbers that add up to, {sum} ? {result} ")

