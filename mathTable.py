'''
# Math table generation for single table
n=int(input("Enter Value:"))

for i in range(1,11):
  print(n,"*",i,"=",n*i)

'''

"""
# Generating math tables up to given range
"""
n=int(input("Enter Value:"))

for i in range(1,n+1):
    for j in range(1,11):
        print(i,"*",j,"=",j*i)
    print("\n")
