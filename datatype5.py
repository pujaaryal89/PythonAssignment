def convert(str):
    convertion=""
    string="ing"
    
    if len(str)<3:
       convertion=str 
    elif str[-3:] not in string:
        convertion=str+'ing'
    elif str[-3:] in string:
        convertion=str.replace("ing","ly")        
            
    return convertion        
            
    



print(convert(input("Enter the word: ")))