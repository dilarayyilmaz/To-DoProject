fruits = ['apple', 'banana', 'cherry', 'orange', 'strawberry', 'kiwi']
# newlist=[]

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
#
# print(newlist)

# newlist=[x for x in fruits if "a" in x]

newlist = [x for x in fruits if x != 'orange']

print(newlist)