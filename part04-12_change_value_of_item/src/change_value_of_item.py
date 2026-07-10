# Write your solution here
holder=[1,2,3,4,5]
while True:
    index=int(input("Index:"))
    if index==-1:
        break
    new=int(input("New value"))
    holder[index]=new
    print(holder)