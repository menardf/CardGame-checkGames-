from sys import argv

filename = argv

txt = open(filename)

print("here is your file %r"%(filename))
print(txt.read())
