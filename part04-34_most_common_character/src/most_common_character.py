# Write your solution here
def most_common_character(text):
    max_count= 0
    common_string=""
    char=text
    for i in text:
        count=0
        while i in text:
            count+=1
            text=text[text.find(i)+1:]
        if count > max_count:
            max_count=count
            common_string=i
        text=char
    return common_string

if __name__=="__main__":
    first_string = "abbbbcdbde"
    print(most_common_character(first_string))



