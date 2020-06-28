a, b = input("Enter a two string: ").split()

string=a.replace(a[:1],b[:1]) + " " +b.replace(b[:1],a[:1])
print(string)