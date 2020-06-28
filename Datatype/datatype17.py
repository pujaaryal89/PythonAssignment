from functools import reduce

mul=lambda x,y: x*y

result=reduce(mul,range(2,6)) #(add,[2,3,4,5])
print(result)