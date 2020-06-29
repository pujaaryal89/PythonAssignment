def max_num(num_list):
    largest_num=num_list[0]
    
    for num in num_list[1:]:
        if num >largest_num:
            largest_num=num
    return largest_num        

number = input('Enter a number separate by comma: ').split(',')
num=[int(x) for x in number]
print(f"The numbers are:{num}")
largest_num=max_num(num)
print(f"The largest numbers is:{largest_num}")


