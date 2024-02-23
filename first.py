def colors():
    for i in ['one','two','three']:
        yield i


for c in colors():
    print(c)

x= colors()
print(x)

print(colors())

n = input("enter number")
fact =1
  # You can replace 10 with any number you want

for i in range(1, n+1):
    # Your code here
    fact = fact * i
    print(i)

import numpy as np
help(np.sort)




