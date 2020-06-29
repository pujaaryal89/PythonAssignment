def add_function(num_list):
    n=sum(num_list)
    return n    
    
number = input('Enter a number separate by comma: ').split(',')
num=[int(x) for x in number]
sum_num=add_function(num)
print(f"The sum of numbers is:{sum_num}")


