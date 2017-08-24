# emotion-recognition

## Reference website
    - http://www.lai18.com/content/9363802.html

## Steps
1. Download Corpus
    - Berlin emotional speech database (Emo-DB)
    URL : http://www.emodb.bilderbar.info/download/
    音檔位置 : D:\EmoDB\wav
    
2. Feature Extraction
    - OpenSMILE is used to extract the LLDs (384 dim)
    URL : http://audeering.com/technology/opensmile/#download
    SMILExtract_Release.exe 位置 : D:\Opensmile\bin\Win32
    IS09_emotion.conf 位置 : D:\Opensmile\config
    
3. Command Line
   切換到 D 槽 -  cd /d d:\
   切換到音檔的目錄 - cd EmoDB\wav
   
4. 編輯 bat 檔 ，把音檔轉成文字檔 ，bat 檔和音檔在同一個目錄 (test.bat 也在相同的目錄)
   bat 檔的內容
   - SMILExtract_Release -C  D:\Opensmile\config\IS09_emotion.conf  -I D:\EmoDB\wav\03a05Aa.wav -O D:\HW2\03a05Aa.txt
     pause
     (對單一音檔)
   - SMILExtract_Release -C  D:\Opensmile\config\IS09_emotion.conf  -I D:\EmoDB\wav\03a05Aa.wav -O D:\HW2\03a05Aa.txt
     pause
     (對許多音檔)
