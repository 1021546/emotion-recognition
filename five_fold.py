# each file(*.txt) divided into 7 fold by emotion , emotion average distribution to file
import os
import types

fold_count = [0, 0, 0, 0, 0] # each fold has data count 
fold_number = 5

emotion_pointer = [0, 0, 0, 0, 0, 0, 0] # seven emotions assigned to five fold

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
	
# def generate_train(inputData,inputName):
    # for i in range(1,11):
        # if i != int(get_speaker(inputName[0:2])):
            # text_file = open("D:/10_fold"+"/train_"+str(i)+".txt", "a")
            # text_file.write(inputData + "\n")
            # text_file.close()
    # return

# def generate_text(inputData,inputName):
    # text_file = open("D:/10_fold"+"/test_"+get_speaker(inputName[0:2])+".txt", "a")
    # text_file.write(inputData + "\n")
    # text_file.close()
    # return
	
def generate_train_file():
    for i in range(0,5):
        loadFile = open("D:/5_fold"+"/test_"+str(i)+".txt", 'r')
        content = loadFile.read() # read all line
        loadFile.close()
        for j in range(0,5):
            if i != j:
                write_file = open("D:/5_fold"+"/train_"+str(j)+".txt", "a")
                write_file.write(content)
                write_file.close()
                
    return
	
def get_file_count():
    fileCount=0
    for filename in os.listdir('.'):
        if os.path.splitext(filename)[-1] == '.txt':
            fileCount+=1;
    return fileCount
	
	

def five_part(inputData,inputName):
    fold_pointer=0
    emotion_index=0
    emotion_index = int(getEmotion(inputName[5]))  # get emotion
    fold_pointer = emotion_pointer[emotion_index-1] # get fold

    while(True): # get real fold
        if fold_count[fold_pointer] >= fold_limit:
            fold_pointer+=1
            if fold_pointer == fold_number:
               fold_pointer = 0
        else:
            break
    
    fold_count[fold_pointer]+=1
	
    if (fold_pointer+1) == fold_number:
        emotion_pointer[emotion_index-1] = 0
    else:
        emotion_pointer[emotion_index-1] = fold_pointer+1 # emotion assigned to next fold
    
    
    text_file = open("D:/5_fold"+"/test_"+str(fold_pointer)+".txt", "a")
    text_file.write(inputData + "\n")
    text_file.close()
    return
	
fold_limit = get_file_count() / fold_number

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
        #print get_file_count()
        #print fold_limit
        five_part(file_context,filename)
        
        # generate_train(file_context,filename)
        # generate_text(file_context,filename)
        # print file_context
        # file_data.append(file_context)
        # print(get_speaker(filename[0:2]))
generate_train_file()	

