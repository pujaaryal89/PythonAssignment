def factorial(number):
    factorial=1
    for n in range(1,number+1):
        factorial=factorial*n
        
    return factorial    
        

number=int(input("Enter the number: "))
numbers=factorial(number)
print(f"The factorial of number is: {numbers}")
