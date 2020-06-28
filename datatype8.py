def remove(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part

print(remove('Python', 3))
print(remove('Python', 5))
