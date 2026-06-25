f= open("sample.txt","r") # file object
data = f.read()

print(data)

print(type(data))

w =open("sample.txt","w")


w.write("text to overwrite \n the complete data ")

f.close()