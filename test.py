# get each file(*.txt) filename
import os
for filename in os.listdir('.'):
    print "Loading: %s" % filename
    if os.path.splitext(filename)[-1] == '.txt':
        print filename