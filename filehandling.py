f = open("myfile.txt", "r")
#print(f.read())
#print(f.readline())
#Aprint(f.readline())
#print(f.read(3))
#f.close()



#with open("myfile.txt") as f:
 #   print(f.read(2))

#with open("myfile.txt") as f:
 #   for x in f:
  #      print(x)

#with open ("myfile.txt", "a") as f:
   # f.write("new data added")

#with open("myfile.txt") as f:
  #  print(f.read())

#f = open("file.txt", "x")

import os
os.remove("file.txt")

if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("not exist")    
