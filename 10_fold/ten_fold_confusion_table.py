import string
import os

path = "C:/Users/cse_ncku/Downloads/hw2/LIBSVM/libsvm-3.22/windows/10_fold"
emotion_num = 7;

for fold in range(0, 10):

    path_fold = path + "/fold_" + str(fold)
    output_context_train = ""
    output_context_test = ""
    confusion_table_train = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    confusion_table_test = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    # train的資料的標記
    file = open(path_fold+'/train.txt', 'r')
    label_train = list()
    for line in open(path_fold+'/train.txt'):
        label_train.append(file.readline()[0:1])
    # print(label_train)
    file.close()

    # train的資料的分類結果
    file = open(path_fold+'/Result_train.txt', 'r')
    result_train = list()
    for line in open(path_fold+'/Result_train.txt'):
        result_train.append(file.readline()[0:1])
    del result_train[0] # delete "labels"
    # print(result_train)
    file.close()

    # test的資料的標記
    file = open(path_fold+'/test.txt', 'r')
    label_test = list()  
    for line in open(path_fold+'/test.txt'):
        label_test.append(file.readline()[0:1])
    # print(label_test)
    file.close()

    # test的資料的分類結果
    file = open(path_fold+'/Result_test.txt', 'r')
    result_test = list()
    for line in open(path_fold+'/Result_test.txt'):
        result_test.append(file.readline()[0:1])
    del result_test[0] # delete "labels"
    # print(result_test)
    file.close()

    # 
    for i in range(0, len(result_train)):
        confusion_table_train[int(label_train[i])-1][int(result_train[i])-1] += 1

    for i in range(0, len(label_test)):
        confusion_table_test[int(label_test[i])-1][int(result_test[i])-1] += 1

    #
    temp = [0, 0, 0, 0, 0, 0, 0]
    for i in range(0, emotion_num):
        for j in range(0, emotion_num):
            temp[i] += confusion_table_train[i][j]

    for i in range(0, emotion_num):
        for j in range(0, emotion_num):
            if temp[i] == 0:
                output_context_train += str(confusion_table_train[i][j]) + "(0.00%) | "
            else:
                output_context_train += str(confusion_table_train[i][j]) + "("+ str("%.2f" %(100*confusion_table_train[i][j]/temp[i])) + "%) | "
        output_context_train += "\n"

    temp = [0, 0, 0, 0, 0, 0, 0]
    for i in range(0, emotion_num):
        for j in range(0, emotion_num):
            temp[i] += confusion_table_test[i][j]

    for i in range(0, emotion_num):
        for j in range(0, emotion_num):
            if temp[i] == 0:
                output_context_test += str(confusion_table_test[i][j]) + "(0.00%) | "
            else:
                output_context_test += str(confusion_table_test[i][j]) + "("+ str("%.2f" %(100*confusion_table_test[i][j]/temp[i]))+ "%) | "
        output_context_test += "\n"

    # 寫入檔案
    write_file = open(path_fold+"/confusion_table_train.txt", "w")
    write_file.write(output_context_train)
    write_file.close()

    write_file = open(path_fold+"/confusion_table_test.txt", "w")
    write_file.write(output_context_test)
    write_file.close()

