def function1(nums):
    
    return list(dict.fromkeys(nums))
    
number=input("Enter the number: ").split(',')
num=[int(x) for x in number]
new_list=function1(num)
print(new_list)