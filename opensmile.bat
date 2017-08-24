for %%i in (*.wav) do (
   D:\Opensmile\bin\Win32\SMILExtract_Release -C D:\Opensmile\config\IS09_emotion.conf -I %%i -O D:\HW2\%%~ni.txt
)
pause 