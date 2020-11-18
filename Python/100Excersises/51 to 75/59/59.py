a = [1, 2, 3] 
# print(item in enumerate(a))
for i in a:
    index=a.index(i)
    print("item "+str(i)+" has index "+str(index))
    # 
# OR    #     # 
for item,index in enumerate(a):
    print("item "+str(item)+' has index '+str(index))