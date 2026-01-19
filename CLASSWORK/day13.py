
text=input("enter the new item :")
f= open("item.py", "a")
f.write("We have added more contents to the file")
f.close()
f=open("item.py", "r")
print(f.read())
print("item is",text)
         
         
         