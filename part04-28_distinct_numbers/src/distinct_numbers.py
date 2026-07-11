# Write your solution here
def distinct_numbers(list):
    distinct=[]
    for i in list:
        if i not in distinct:
            distinct.append(i)
    distinct.sort()
    return distinct

