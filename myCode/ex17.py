from sys import argv
from os.path import exists #这个命令将 文件名字符串作为参数，如果文件存在的话，它将返回 True，否则将返回 False

script,from_file,to_file=argv,"test.txt","copied.txt"

print("Copying from %s to %s" % (from_file,to_file))
inputt=open(from_file)
indata=inputt.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready,hit RETURN to continue,CTRL-C to abort.")
input()

output=open(to_file,'w')
output.write(indata)

print("Alright,all done.")

output.close()
inputt.close()
