def function(num): 
    for i in range(2,num):   
     if num % i == 0:
        print(" not prime")
        break
    else: 
        print("prime")
    return num      
        

prime_num=int(input("Enter the number:"))
num=function(prime_num)


