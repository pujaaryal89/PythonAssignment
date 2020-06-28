from functools import reduce

add=lambda x,y: x+y

result=reduce(add,range(2,6)) #(add,[2,3,4,5])
print(result)
    
