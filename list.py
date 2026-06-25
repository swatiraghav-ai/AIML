marks=[34,56,76,85,34,"abc",24.32]
print (len(marks))
print(marks[3])
marks[3]=90
print(marks[0:5])
marks.append(100)
print(marks)
marks.insert(2,45)
print(marks)
nums=[1,2,3,4,5]
x=3
idx=0
for i in nums:
    if (i==x):
        print(idx)
        break
    idx+=1
    
