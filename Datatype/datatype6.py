def change(x):
    words="not poor"
    word="poor"
    if x in words or word:
        x=x +x.replace(word,words,'gold')
    
    return x 

     
print(change(input("Enter the word: ")))
