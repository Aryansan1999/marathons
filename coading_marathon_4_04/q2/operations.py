from io import TextIOBase
def word_occurance(f:TextIOBase):
    lines=f.readlines()
    count=0
    data=[]
    print(lines)
    for line in lines:
        s=""
        for char in line:
            s=s+char
            if char==" ":
                
                data.append(s)
                s=""
    
    for list_data in data:
        for cheak_data in data:
            if list_data==cheak_data:
                count+=1
        print(f"{list_data}: {count}")
        count=0
    return 


def line_length(f:TextIOBase):
    lines=f.readlines()
    for words in lines:
        count=0
        for chars in words:
            if chars!=" ":
                count+=1
        print(f"Length of line is: {count}")
    return
        
def first_N_lines(f:TextIOBase,N:int):
    lines=f.readlines()
    for line in range(len(lines)):
        if line<N:
            print(lines[line])
    return

path=r"/home/aryans2/Desktop/coading_marathon_4_04/q2/sample_data.txt"
with open(path,'r') as f:
    
    # word_occurance(f)
    # line_length(f)
    n=int(input("Enter value of N"))
    first_N_lines(f,n)