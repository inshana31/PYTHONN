import re
try:
   title=input("entr the book name")
   if not re.match(r'^[A-Za-z ]+$', title):
      raise ValueError("Error: Book title must contain only alphabets and spaces.")
   year=input("entr the year ")
   if not re.match(r'^(19|20)\d{2}$', year):
      raise ValueError("error:year  is not in the prpr format")
except:
   print(ValueError) 
else:
           print("\nProgram finished. Thank you for using the mini library system!")

   

   

   
   