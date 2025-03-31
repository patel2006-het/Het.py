
names = [("het",), "riya", ("Aditya",), "priya", ("Manav",), "tina", "rina"]

# Initialize counters
boys_count = 0
girls_count = 0

for name in names:
    if isinstance(name, tuple):  
        boys_count += 1
    else: 
        girls_count += 1

#  result
print("Number of boys:", boys_count)
print("Number of girls:", girls_count)
