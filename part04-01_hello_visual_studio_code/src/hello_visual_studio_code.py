# Write your solution here
while True:
    choice=input("Editor:").lower()
    if choice=="visual studio code":
        print("an excellent choice!")
        break
    elif choice in ["word","note pad"]:
        print("awful")
    else:
        print("not good")