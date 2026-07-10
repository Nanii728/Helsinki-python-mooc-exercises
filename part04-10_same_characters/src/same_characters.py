# Write your solution here
def same_chars(word,ind1,ind2):
    if (ind2 < len(word))and (ind1 < len(word)):
        return word[ind1] == word[ind2]
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("abracadabra", 0, 3))