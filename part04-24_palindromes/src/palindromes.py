# Write your solution here
def palindromes(x:str)->bool:
    if x==x[::-1]:
        return True
    else:
        return False
while True:
    text=input("Please type in a palindrome:")
    if palindromes(text):
        print(f"{text} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")


# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
    print(palindromes("hana"))
 
