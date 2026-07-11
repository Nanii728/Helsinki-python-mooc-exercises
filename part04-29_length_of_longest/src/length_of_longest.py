# Write your solution here
def length_of_longest(list):
    max_length=0
    for i in list:
        if len(i)>max_length:
            max_length=len(i)
    return max_length