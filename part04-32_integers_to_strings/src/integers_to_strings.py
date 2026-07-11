# Write your solution here
def formatted(items):
    new_list=[]
    for i in items:
        new_list.append(f"{i:.2f}")
    return new_list