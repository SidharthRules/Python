import os

# Create a Directory and make it working dir.
os.mkdir("test")
os.chdir("test")
print "current working Dir: ",os.getcwd()
name=raw_input("Give the Name: ")

# Open a file and writing into it
fo = open(name, "w+")
fo.write(raw_input("Give the Data : "))
fo.close()

# Open a file and reading it
fo = open(name, "r+")
str = fo.read();
print "Read The Data :",str
fo.close()
