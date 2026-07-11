# Write your solution here
def anagrams(x:str,y:str)->bool:
    if sorted(x)==sorted(y):
        return True
    else:
        return False

if __name__=="__main__":
    print(anagrams("hana","text"))
    print(anagrams("pii","ip"))