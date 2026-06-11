info=[
("swati" , "science"),
("ravi","maths"),
("sita","english"),
("gita","maths"),
("palak","english"),
("swati","english"),
("palak","science"),
]
unique_courses=set()
for tup in info:
    print(tup[1])
    unique_courses.add(tup[1])
print(unique_courses)

for course in info:
    if(course[1]=="english"):
        print(course[0])
dict={}
for name,course in info:
    if (dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
      dict[name].add(course)

print(dict)        

