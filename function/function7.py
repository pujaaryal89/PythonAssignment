def check_function(str):
    count1=0
    count2=0
    for n in str:
        if (n.isupper()):
            count1+=1
            
        elif (n.islower()):
            count2+=1
    print("the uppercase is :",count1)                   
    print("the lowercase is :",count2)                   
                       
string=input("Enter the string: ")
strings=check_function(string)


