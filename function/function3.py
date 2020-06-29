def multiplication_function(num_list):
    result = 1
    for x in num_list: 
         result = result * x  
    return result    
       
number = input('Enter a number separate by comma: ').split(',')
num=[int(x) for x in number]
mul_num=multiplication_function(num)
print(f"The multiplication of numbers is:{mul_num}")
