# Write your solution here
holder=[]
print("The list is now []")
while True:
    choice=input("a(d)d, (r)emove or e(x)it:")
    if choice=='d':
        if len(holder)==0:
            holder.append(1)
        else:
            holder.append(holder[-1] + 1)
    elif choice=='r':
        holder.pop()
    elif choice=='x':
        print("Bye!")
        break
    print(f"The list is now {holder}")


