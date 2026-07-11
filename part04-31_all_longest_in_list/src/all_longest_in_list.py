# Write your solution here
def all_the_longest(items):
    long=""
    list_of_long=[]
    for i in items:
        if len(i)>len(long):
            long=i

    for i in items:
        if len(long)==len(i):
            list_of_long.append(i)

    return(list_of_long)
