def translate(word):
    translation="" 
    if len(word)>=2:
        translation=translation+word[0:2] + word[-2:] 
    else:    
        print("invalid")  
            
    return translation

print(translate(input("Enter the word: ")))
        

 
    
    
 
    
   
        
   
    
             
