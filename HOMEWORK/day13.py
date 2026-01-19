
names = input("Enter names separated by space: ").split()
print("list of Names:", names)
f=open("students.txt","a")
f.write("mera, jasmin,lekha")
f.close()
f=open("students.txt","r")

f = open("students.txt", "r")
for x in f:
  print(x)
print(f.read())
