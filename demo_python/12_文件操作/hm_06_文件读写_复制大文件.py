"""
    打开一个已有文件，逐行读取内容，并顺序写入到另外一个文件
"""


file_read = open("README.txt")
file_write = open("README_copy2.txt", "w")

while True:
    text = file_read.read()

    if not text:
        break

    file_write.write(text)


file_read.close()
file_write.close()
