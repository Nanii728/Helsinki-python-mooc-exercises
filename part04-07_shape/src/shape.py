# Copy here code of line function from previous exercise and use it in your solution
def line(num,char):
    if len(char)>0:
        print(char[0]*num)
    else:
        print("*" * num)

# You can test your function by calling it within the following block

def shape(width,tr_char,height,rec_char):
    for i in range(1,width+1):
        line(i, tr_char)
    
    for i in range(height):
        line(width, rec_char)

if __name__ == "__main__":
    shape(5, "x", 3, "*")