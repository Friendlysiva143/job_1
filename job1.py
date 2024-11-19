import random
l=[]
for i in range(10):
    ele=random.randint(10,100)
    l.append(ele)
print("the created list",l)
print("the sum of list is :",sum(l))
print("the minium in the list is :",min(l))
print("the maximum in the list is:",max(l))