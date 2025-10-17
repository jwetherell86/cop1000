db = open("output.txt", "a")
a = "Hello"+str(1)
b = "How do you do?"
db.write(a+", "+b+"\n")
db.close()