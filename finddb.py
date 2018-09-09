#!/home/jack/anaconda2/envs/py35/bin/python
import os
f = open("sqlitedatabases.txt", "r").readlines()
f0 = open("sqlitedatabases-size.txt", "w")
for line in f:
    line = line.replace("\n","")
    sz = os.path.getsize(line)
    sz=str(sz)
    f0.write(line+', '+sz+'\n')
f0.close()    