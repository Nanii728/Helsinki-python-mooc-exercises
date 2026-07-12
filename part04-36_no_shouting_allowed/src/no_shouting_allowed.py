# Write your solution here
def no_shouting(items):
    pruned_list=[]
    for i in items:
        if i.isupper():
            continue
        else:
            pruned_list.append(i)
    return pruned_list
