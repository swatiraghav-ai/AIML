word ="python"
print(word[-4:-2])

# formating
a=5
b=10
sum=a+b
#normal formating
print("sum is {}".format(sum))
print ("sum of {} & {} is {}".format(a,b,sum))
# index based formating
print ("sum of {1} & {0} is {2}".format(a,b,sum))
# value based formating
print ("sum of {name1} & {name2} is {result}".format(name1=a,name2=b,result=sum))