"""
    按行读取文件内容
"""
"""
    * `read` 方法默认会把文件的 **所有内容** **一次性读取到内存**
    * 如果文件太大，对内存的占用会非常严重
"""
"""
    `readline` 方法
        * `readline` 方法可以一次读取一行内容
        * 方法执行后，会把 **文件指针** 移动到下一行，准备再次读取
"""


file = open("README.txt") # 默认为只读

while True:
    text = file.readline()

    # 判断读取的内容是否为空
    if not text:
        break

    print(text)


file.close()

