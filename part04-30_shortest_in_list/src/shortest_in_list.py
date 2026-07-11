# Write your solution here
def shortest(items):
    min_length=len(items[0])
    short=""
    for i in items:
        if len(i)<min_length:
            min_length=len(i)
            short=i
    return short

if __name__=="__main__":
    print(shortest(["abc", "ab"]))