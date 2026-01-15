name=input("enter ur name")
feed=input("entr ur feedbacks")
try:
   if not name.strip() or not feed.strip():
      raise ValueError("invalid input please enter the details")
   print(f"thank you  {name}❤️!")
   print(f"Name: {name}")
   print(f"Feedback: {feed}")
   
except:
   print("error occured")

   
finally:
   print("THANK YOU Have a nys day😁\nprogram finish")