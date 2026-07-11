# Write your solution here
choice=int(input("Please type in a positive integer:"))
for i in range(-1*choice,choice+1):
    if i==0:
        continue
    else:
        print(i)