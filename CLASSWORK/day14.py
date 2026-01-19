import random
import math
def reverse(str):
   str=" ".join(reversed(str)) 
   return str 
a="mekha"
print("the reversed string is:",reverse(a))
user = "maya","neha","priya","maya","achu","neha"
print ("The original list is : " +  str(user)) 
result = [] 
[result.append(x) for x in user if x not in result] 
print ("The list after removing duplicates : " + str(result)) 
print("random element: ",random.choice(user))

unique=list(set(user))
total=len(unique)
print("the unique is:",total)
rounds=round(math.sqrt(total))
print("rounded value:",rounds)


print("THanku for playing game")