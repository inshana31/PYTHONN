item=["milk", "bread", "eggs"]


def add_item(item):
   new_item=item.append("coffee")
   return item
print(add_item(item))

def remove_last_item(item):
   del_item=item.pop()
   return item
print(remove_last_item(item))

display_item = lambda item: print(f"Item: {item}")
display_item(item)


def recurse(item):
   if not item:  
      return 0
   return len(item[0]) + recurse(item[1:])


print("Total characters:",recurse(item))
