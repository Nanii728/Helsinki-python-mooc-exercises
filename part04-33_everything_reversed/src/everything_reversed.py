# Write your solution here
def everything_reversed(items):
    new_list=[]
    for i in items:
        new_list.insert(0,i[::-1])
    return new_list