import os # used for make file and folder

if not os.pathexists ("dragon")# to check folder exists or not
os.mkdir("dragon")


print("the current location")
print(os.getcwd())


print('the current directory content')
content = os.listdir()
print (content)



print('size of file', os.path.getsize('set.ipynb')/1024,'MB')