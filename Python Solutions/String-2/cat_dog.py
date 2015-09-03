"""Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True"""

def cat_dog(str):
    
    cats = 0
    dogs = 0 
    
    for i in range(len(str)-2):
        if str[i:i+3] == "cat":
            cats += 1
        if str[i:i+3] == "dog":
            dogs += 1
    
    if dogs == cats:
        return True
    else:
        return False
  
