# get each file(*.txt) Speaker
import os
import types
# import string

file_data = []

def getEmotion(x):
	# 'W' => anger, 'L' => boredom, 'E' => disgust, 'A' => anxiety/fear, 'F' => happiness, 'T' => sadness, 'N' => neutral version
    return {
        'W': "1",
        'L': "2",
        'E': "3",
        'A': "4",
        'F': "5",
        'T': "6",
        'N': "7"
    }.get(x, "0") 
	
def get_speaker(x):
    return {
        '03': 0,
        '08': 1,
        '09': 2,
        '10': 3,
        '11': 4,
        '12': 5,
        '13': 6,
        '14': 7,
        '15': 8,
        '16': 9
    }.get(x, 0) 


def addNumber(inputList):
    for i in range(0, len(inputList)):
        inputList[i] = str(i+1) + ":" + inputList[i] + " "
    return

def combineList(inputList,inputName):
    context = getEmotion(inputName[5]) + " "
    for i in range(0, len(inputList)):
        context += inputList[i]
    return	context


for filename in os.listdir('.'):
    #print "Loading: %s" % filename
    if os.path.splitext(filename)[-1] == '.txt':
        #print filename
        loadFile = open(filename, 'r')
        lines = loadFile.readlines() # read all line
        last_line = lines[-1] # get last line
        #print last_line
        last_line = last_line[10:-3].split(",") #remove " 'unknown', " and " ,? " then splited by ","
        addNumber(last_line)
        loadFile.close()
        file_context = combineList(last_line,filename)
        # print file_context
        file_data.append(file_context)
        print(get_speaker(filename[0:2]))
		

# print file_data[0]
# print file_data[1]
# print file_data[2]