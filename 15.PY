# Create a list of tuples containing a food item and its price. Sort the tuples in descending order by price
food_item=[(300,"pizza"),(250,"sizzler"),(40,"vadapau"),(60,"burger"),(400,"salad")]

newlist=list(food_item)

newlist.sort()
newlist.reverse()
food_item=tuple(newlist)
print(food_item)






