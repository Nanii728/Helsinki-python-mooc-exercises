# Write your solution here
items=[]
number=int(input("How many items:"))
for i in range(number):
    item=int(input(f"Item {i+1}:"))
    items.append(item)
print(items)
