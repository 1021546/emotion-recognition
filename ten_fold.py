# each file(*.txt) divided into 10 fold by Speaker
import os
import types
# import string

file_data = ["", "", "", "", "", "", "", "", "", ""]

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
        '03': "1",
        '08': "2",
        '09': "3",
        '10': "4",
        '11': "5",
        '12': "6",
        '13': "7",
        '14': "8",
        '15': "9",
        '16': "10"
    }.get(x, "0") 


def addNumber(inputList):
    for i in range(0, len(inputList)):
        inputList[i] = str(i+1) + ":" + inputList[i] + " "
    return

def combineList(inputList,inputName):
    context = getEmotion(inputName[5]) + " "
    for i in range(0, len(inputList)):
        context += inputList[i]
    return	context
	
def generate_train(inputData,inputName):
    for i in range(1,11):
        if i != int(get_speaker(inputName[0:2])):
            text_file = open("D:/10_fold"+"/train_"+str(i)+".txt", "a")
            text_file.write(inputData + "\n")
            text_file.close()

def generate_text(inputData,inputName):
    text_file = open("D:/10_fold"+"/test_"+get_speaker(inputName[0:2])+".txt", "a")
    text_file.write(inputData + "\n")
    text_file.close()

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
		
        generate_train(file_context,filename)
        # generate_text(file_context,filename)
        # print file_context
        # file_data.append(file_context)
        # print(get_speaker(filename[0:2]))
		

# print file_data[0]
# print file_data[1]
# print file_data[2]