dic1={"num1":5}
dic2={"num2":6}
new_dict={}
for d in (dic1, dic2): new_dict.update(d)
print(new_dict)