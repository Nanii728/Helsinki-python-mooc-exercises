# Write your solution here
def no_vowels(text):
    items=text.split()
    result=[]
    for k in items:
        for i in ["a","e","i","o","u"]:
            while i in k:
                k=k.replace(i,"")
        result.append(k)
        
    return " ".join(result)

if __name__=="__main__":
    print(no_vowels("this is an example"))
