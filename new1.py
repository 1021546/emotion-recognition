# split each file(*.txt) last line by ","
import os
import types

file_data = []

for filename in os.listdir('.'):
    #print "Loading: %s" % filename
    if os.path.splitext(filename)[-1] == '.txt':
        #print filename
        loadFile = open(filename, 'r')
        lines = loadFile.readlines() # read all line
        last_line = lines[-1] # get last line
        #print last_line
        last_line = last_line[10:-3].split(",") #remove " 'unknown', " and " ,? " then splited by ","
        #print type(last_line)
        file_data.append(last_line)	
        loadFile.close()
		

print file_data[0]
print file_data[1]
print file_data[2]