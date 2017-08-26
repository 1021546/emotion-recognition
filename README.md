# emotion-recognition

## Reference website
    - http://www.lai18.com/content/9363802.html

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
    
3. Command Line
   切換到 D 槽 -  cd /d d:\
   切換到音檔的目錄 - cd EmoDB\wav
   
4. 編輯 bat 檔 ，把音檔轉成文字檔 ( bat 檔和音檔在同一個目錄 ，test.bat 也在相同的目錄 )
   bat 檔的內容
   - (對單一音檔)
     D:\Opensmile\bin\Win32\SMILExtract_Release -C D:\Opensmile\config\IS09_emotion.conf -I D:\EmoDB\wav\03a05Aa.wav -O D:\HW2\03a05Aa.txt
   
     pause
     
   - (對許多音檔) opensmile.bat

5. Command Line
   切換到 HW2 目錄 -  cd D:\HW2
   
6. 編輯 python 檔 ( python 檔位置在 D:\HW2 ，test.py 和 data.py 和 new1.py 和 new2.py 和 new3.py 和 new4.py 也在相同的目錄 ) ，擷取最後一行的
   資料
   -ten_fold.py 和 five_fold.py
   
7. 執行 python 檔
   -ten_fold.py 和 five_fold.py
   執行 ten_fold.py 在 D:\10_fold 目錄底下產生 train_1~10.txt 和 test_1~10.txt
   執行 five_fold.py 在 D:\5_fold 目錄底下產生 train_1~5.txt 和 test_1~5.txt
   
8. 在位置 : D:\LibSVM\libsvm-3.22\windows 目錄底下執行 svm

## Learned
1. windows command 移除檔案 - del *.txt
