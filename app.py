from user import User

p1 = User("John", "36","5665464")

a = 6
b = 8

a += 1 
b -= 1

c = a * b

a = 6
b = 8

++a
--b

d = a * b
print(c)
print(d)
if c != d:
  print(" Double increment or decrement gives bugs ")
else:
  print("ok")  

p1.myfunc()