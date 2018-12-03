from sys import argv #导入

script,filename=argv,"ex15_sample.txt"
txt=open(filename) #打开文件命令
print("Here's your file %r:" % filename)
print(txt.read())#读出文件内容
print("Type the filename again:")
file_again=input("> ")
txt_again=open(file_again)
print(txt_again.read())
txt.close()
txt_again.close()
