# check file whether the average distribution emotion

import os


count = [0, 0, 0, 0, 0, 0, 0]

def calculate_number(inputList):
	index=0
	for i in range(len(inputList)):
		index = int(inputList[i])
		count[index-1]+=1
	write_file = open("D:/5_fold/check_result.txt", "a")
	for i in range(len(count)):
		write_file.write(str(i+1)+" : "+str(count[i])+"\n")
	write_file.write("-------------------------------------------------------------------"+"\n")
	write_file.close()

for filename in os.listdir('.'):
	if os.path.splitext(filename)[-1] == '.txt':
		result = list()
		loadFile = open(filename, 'r')
		#print filename
		lines = len(loadFile.readlines())
		# print lines
		loadFile.seek(0)
		for i in range(0,lines):
			result.append(loadFile.readline()[0:1])
		loadFile.close()
		# print result

		calculate_number(result)



