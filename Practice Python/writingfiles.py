"""To write a file, you have to open it with mode “w” as a second parameter:
If the file already exists, opening it in write mode clears out the old data and starts
fresh, so be careful! If the file doesn’t exist, a new one is created.
The write method of the file handle object puts data into the file, returning the
number of characters written. The default write mode is text for writing (and
reading) strings.
"""
# \
fout = open("test1.txt","w")
line1 = "This here's the wattle, ¥n"
line2 ="the emblem of our land.¥n"
fout.write(line1)
fout.write(line2)
fout.close()

