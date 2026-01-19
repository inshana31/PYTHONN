import random
import math
user=input("enter the names (comma seperater)")
print(user)
result = [] 
for x in user: 
    if x not in result: 
        result.append(x) 
print ("The list after removing duplicates : " + str(result)) 
print("random element: ",random.choice(user))
def reverse(string): 
    string = "".join(reversed(string)) 
    return string 
print ("The original string  is : ",user)  
print ("The reversed string(using reversed) is : ",reverse(user)) 
print("The winners is",random.choices(user,k=2))

unique=list(set(user))
total=len(unique)
print("the unique is:",total)
rounds=round(math.sqrt(total))
print("rounded value:",rounds)