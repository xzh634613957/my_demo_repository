"""
    安装删除包
"""
"""
    安装包:
        1. tar -zxvf hm_message-1.0.tar.gz 
        2. sudo python3 setup.py install
"""
"""
    删除包:
        直接从安装目录下，把安装模块的 **目录** 删除就可以(可以用 hm_message.__file__ 来查看包的目录)
        1. cd /usr/local/lib/python3.5/dist-packages/
        2. sudo rm -r hm_message*
"""