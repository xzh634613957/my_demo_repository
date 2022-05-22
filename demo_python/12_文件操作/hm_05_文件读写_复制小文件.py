"""
    用代码的方式，来实现文件复制过程
"""
"""
    打开一个已有文件，读取完整内容，并写入到另外一个文件
"""


file_read = open("README.txt")
file_write = open("README_copy.txt", "w")


text = file_read.read()
file_write.write(text)


file_read.close()
file_write.close()
