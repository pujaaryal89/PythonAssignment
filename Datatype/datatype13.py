items = input("Write the name :")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))