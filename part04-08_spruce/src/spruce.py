# Write your solution here
def spruce(num):
    print("a spruce!")
    for i in range(num):
        print(f"{" " *(num-i-1)}{"*"*(2*i + 1)}")
    print(f"{" " * (num-1)}*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)