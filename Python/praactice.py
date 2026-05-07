with open("requirement.txt", "r") as file:
    content=file.read()
    print(content)

with open("example.txt","w") as file: #overwrite mode
    file.write(("Hello world!\n"))

#write withount overwriting
with open("example.txt","a") as file: #append mode
    file.write("Welcome to Python programming.\n")


## binary mode
data=b'\x00\x01\x02\x03\x04\x05'
with open("example2.bin","wb") as file:
    file.write(data)

#move the cursor to the begining
# file.seek(0)    

##create directory
import os
directory1="Python"
os.mkdir("directory1")

#joining paths
import os
path1="C:/Rajeshwari/Udemy Data Science"
path2="Python"
full_path=os.path.join(path1,path2)
print(full_path)

#getting absolute path
relative_path="requirement.txt"
absolute_path=os.path.abspath(relative_path)
print(absolute_path)

try:
    a=10/0
except ZeroDivisionError as ex:
    print("Error:",ex)
else:
    print("No error occurred.",a)

finally:
    print("Execution completed.")