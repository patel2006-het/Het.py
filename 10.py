def add_many(*bkl):
  s = 0
  for v in bkl:
    if type(v) == int or type(v) == float:
      s = s + v
  return s


print(add_many(10, 20, 30, 40, 50))

def print_items(name = 'Darshit', bg = 'O+ve'):
  print(name, bg)
d = { 'name' : 'Ragi', 'bg' : 'A+ve' }
print_items(*d) 
print_items(**d) 

d = dict()

print_items(**d)