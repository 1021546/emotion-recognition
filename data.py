# get each file(*.txt) last line
import os

file_data = []

for filename in os.listdir('.'):
    #print "Loading: %s" % filename
    if os.path.splitext(filename)[-1] == '.txt':
        #print filename
        loadFile = open(filename, 'r')
        lines = loadFile.readlines() # read all line
        last_line = lines[-1] # get last line
        #print last_line
        file_data.append(last_line)	
        loadFile.close()
		
print file_data[0]
print file_data[1]
print file_data[2]