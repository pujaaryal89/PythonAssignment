def my_function(x):
      return list(dict.fromkeys(x))

mylist = my_function(["1", "2", "3", "4", "1"])

print(mylist)   

# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist) 