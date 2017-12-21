import os
print("当前目录是："+os.getcwd())
# os.chdir("D:\\firstdemos\\tmp")
# 或者写法为D:/firstdemos/tmp ,\ 符号是转义符号，所以不能直接写成D:\firstdemos\tmp
# print("修改后的当前目录是："+os.getcwd())
the_file=open("test.txt")
#for the_line in the_file:
#    print(the_line,end='')
#the_file.close()

for the_line in the_file:
    (datapiece,datavalue)=the_line.split("=")
    print(datapiece,end='')
    print("is"+datavalue,end='')




