# emotion-recognition

## Reference website
    - http://www.lai18.com/content/9363802.html
    - http://ntu.csie.org/~piaip/svm/svm_tutorial.html#
    - https://sls.weco.net/blog/hornacik/01-jan-2009/12026

## Steps
1. Download Corpus
    - Berlin emotional speech database (Emo-DB)
    URL : http://www.emodb.bilderbar.info/download/
          http://emodb.bilderbar.info/docu/
    音檔位置 : D:\EmoDB\wav
    
2. Feature Extraction
    - OpenSMILE is used to extract the LLDs (384 dim)
    URL : http://audeering.com/technology/opensmile/#download
    SMILExtract_Release.exe 位置 : D:\Opensmile\bin\Win32
    IS09_emotion.conf 位置 : D:\Opensmile\config
    如果執行時，顯示缺少 dll 檔，那把 msvcp100.dll 和 msvcr100.dll 兩個檔案放到和 SMILExtract_Release.exe 相同位置 : D:\Opensmile\bin\Win32

3. Download LIBSVM
   URL : https://www.csie.ntu.edu.tw/~cjlin/libsvm/
   
4. Command Line
   切換到 D 槽 -  cd /d d:\
   切換到音檔的目錄 - cd EmoDB\wav
   
5. 編輯 bat 檔 ，把音檔轉成文字檔 ( bat 檔和音檔在同一個目錄 ，test.bat 也在相同的目錄 )
   bat 檔的內容
   - (對單一音檔)
     D:\Opensmile\bin\Win32\SMILExtract_Release -C D:\Opensmile\config\IS09_emotion.conf -I D:\EmoDB\wav\03a05Aa.wav -O D:\HW2\03a05Aa.txt
   
     pause
     
   - (對許多音檔) opensmile.bat

6. Command Line
   切換到 HW2 目錄 -  cd D:\HW2
   
7. 編輯 python 檔 ( python 檔位置在 D:\HW2 ，test.py 和 data.py 和 new1.py 和 new2.py 和 new3.py 和 new4.py 和 new5.py 和 new6.py 和 new7.py也在相同的目錄 ) ，擷取最後一行的資料
   -ten_fold.py 和 five_fold.py
   
8. 執行 python 檔
   -ten_fold.py 和 five_fold.py
   執行 ten_fold.py 在 D:\10_fold 目錄底下產生 train_1~10.txt 和 test_1~10.txt
   執行 five_fold.py 在 D:\5_fold 目錄底下產生 train_1~5.txt 和 test_1~5.txt
   ( check_file.py 也在 D:\5_fold 目錄底下 )
   
9. 在位置 : D:\LibSVM\libsvm-3.22\windows 目錄底下執行 svm
   - 必須把 train_1~10.txt 和 test_1~10.txt 搬到 D:\LibSVM\libsvm-3.22\windows 目錄底下
     然後把 train_1~10.txt 和 test_1~10.txt 分別改名成 train.txt 和 test.txt ，為了後面 Command Line 執行方便
     還有把 D:\LibSVM\libsvm-3.22\tools 目錄底下的 grid.py 搬到 D:\LibSVM\libsvm-3.22\windows 目錄底下
     
10. Command Line
svm-scale.exe -s scale train.txt > train.scale
svm-scale.exe -r scale test.txt > test.scale
python grid.py train.scale
svm-train.exe -b 1 -c 2.0 -g 0.125 train.scale
svm-predict.exe -b 1 train.scale train.scale.model Result_train.txt > Accuracy_train.txt
svm-predict.exe -b 1 test.scale train.scale.model Result_test.txt > Accuracy_test.txt

※第4行的參數 (-c 2.0 -g 0.125) 由第3行的執行結果填入。

## Learned
1. windows command 移除檔案 - del *.txt
