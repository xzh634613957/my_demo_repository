## 基于VSCode和CMake进行C/C++开发



### 一、Linux系统介绍

#### 1.1 Linux目录结构

![图片](https://mmbiz.qpic.cn/mmbiz_png/NSZJKGNrtpdRPOo8IDpFUJMUmmZWd6pr8JnrLWyfmy5J6WibqibdLzTVERDNZG3mnAnTIFlm0muVpRNgdDTIs7fA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**Bin：**全称binary，含义是二进制。该目录中存储的都是一些二进制文件，文件都是可以被运行的。

**Dev**：该目录中主要存放的是外接设备，例如盘、其他的光盘等。在其中的外接设备是不能直接被使用的，需要挂载（类似window下的分配盘符）。

**Etc**：该目录主要存储一些配置文件。

**Home**：表示“家”，表示除了root用户以外其他用户的家目录，类似于windows下的User/用户目录。

**Proc**：全称process，表示进程，该目录中存储的是Linux运行时候的进程。

**Root**：该目录是root用户自己的家目录。

**Sbin**：全称super binary，该目录也是存储一些可以被执行的二进制文件，但是必须得有super权限的用户才能执行。

**Tmp**：表示“临时”的，当系统运行时候产生的临时文件会在这个目录存着。

**Usr**：存放的是用户自己安装的软件。类似于windows下的program files。

**Var**：存放的程序/系统的日志文件的目录。

**Mnt**：当外接设备需要挂载的时候，就需要挂载到mnt目录下。

![img](https://mmbiz.qpic.cn/mmbiz_png/NSZJKGNrtpdRPOo8IDpFUJMUmmZWd6prWbPuibUnsXz5DTC7jN9LFgVMEbQBgcg0voQQbwEfFhtCP8PuYn5ia0pg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)



#### 1.2 VIM编辑器

![图片](https://mmbiz.qpic.cn/mmbiz_png/NSZJKGNrtpdRPOo8IDpFUJMUmmZWd6prFYcgoGELI6WbczdNuXxMnd9Wiarx4KBmOd4AT1dvVeWL2m81fRH8Vyg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)



### 二、开发环境搭建

#### 2.1 编译器、调试器安装

```shell
# 安装gcc，g++编译器和gdb调试器
sudo apt install build-essential gdb
# 查看安装版本
gcc --version
g++ --version
gdb --version

# cmake安装
sudo apt install cmake
# 查看安装版本
cmake --version
```



### 三、GCC编译器

- **GCC 编译器**支持编译 Go、Objective-C，Objective-C ++，Fortran，Ada，D 和 BRIG（HSAIL）等程序；
- Linux  开发C/C++ **一定**要熟悉 GCC
- **VSCode是通过调用GCC编译器来实现C/C++的编译工作的；**

实际使用中：

- **使用 gcc 指令编译 C 代码**

- **使用 g++指令编译 C++ 代码**

  

#### 3.1 编译过程

- 利用编译程序从源语言编写的源程序产生目标程序的过程
-  编译就是把高级语言变成计算机可以识别的2进制语言

- 一个cpp文件是如何通过g++命令一步一步地编译成我们所需要的可执行文件的
- 预处理 -> 编译 -> 汇编 -> 链接
- 源代码(.i) -> 汇编代码(.s) -> 二进制代码(.o) -> 可执行程序 

1. **预处理** (Pre-Processing)  ---  .i 文件

   ```shell
   # 对源文件中的头文件、宏定义等进行预处理
   # 预处理后生成 .i 文件
   # 格式：g++ -E [源文件名] -o [预处理后的文件名]
   # -E 选项指示编译器仅对输入文件进行预处理
   g++ -E test.cpp -o test.i
   ```

2. **编译** (Compiling)  ---  .s 文件

   ```shell
   # 将源文件转换成汇编代码的过程
   # 具体的步骤主要有：词法分析 -> 语法分析 -> 语义分析及相关的优化 -> 中间代码生成 -> 目标代码生成（汇编代码文件.s）
   # 格式：g++ -S [预处理文件名] -o [汇编文件名]
   # -S 选项告诉g++在产生汇编代码文件后停止编译
   g++ -S test.i -o test.s
   ```

3. **汇编** (Assembling)  ---  .o 文件

   ```shell
   # 在汇编阶段，汇编器将之前的汇编代码文件转成可重定位的目标程序，即二进制的目标代码 .o文件
   # 格式：g++ -C [汇编文件名] -o [二进制文件名]
   g++ -c test.s -o test.o
   ```

4. **链接** (Linking)  ---  bin 文件

   ```shell
   # 将目标文件、启动代码、库文件链接成可执行文件的过程，这个文件可被加载或拷贝到存储器执行
   # 格式：g++ [二进制文件名] -o [可执行文件]
   g++ test.o -o test
   ```

5. **可以直接使用以下命令将源文件编译为可执行文件**

   ```shell
   g++ test.cpp -o test
   ```

   

#### 3.2 g++重要的编译参数

1. -g --- 编译带调试信息的可执行文件

   ```shell
   # -g 选项告诉 GCC 产生能被 GNU 调试器GDB使用的调试信息，以调试程序（否则无法用GDB调试）
   g++ -g test.cpp -o test
   ```

2. -O[n] --- 优化源代码

   ```shell
   # 所谓优化，例如省略掉代码中从未使用过的变量、直接将常量表达式用结果值代替等等，这些操作会缩减目标文件所包含的代码量，提高最终生成的可执行文件的运行效率
   # -O 选项告诉 g++ 对源代码进行基本优化。这些优化在大多数情况下都会使程序执行的更快。 -O2 选项告诉 g++ 产生尽可能小和尽可能快的代码。 如-O2，-O3，-On（n 常为0–3）
       # -O 同时减小代码的长度和执行时间，其效果等价于-O1
       # -O0 表示不做优化
       # -O1 为默认优化
       # -O2 除了完成-O1的优化之外，还进行一些额外的调整工作，如指令调整等
       # -O3 则包括循环展开和其他一些与处理特性相关的优化工作。
   # 选项将使编译的速度比使用 -O 时慢， 但通常产生的代码执行速度会更快
   
   # 使用 -O2优化源代码，并输出可执行文件
   g++ -O2 test.cpp -o 
   ```

3. -l & -L --- 指定库文件 & 指定库文件路径

   ```shell
   # -l 参数(小写)就是用来指定程序要链接的库，-l 参数紧接着就是库名
    # 在/lib、/usr/lib、/usr/local/lib里的库直接用-l参数就能链接
    # case:  链接glog库
    g++ -lglog test.cpp
   
    # 如果库文件没放在上面三个目录里，需要使用-L参数(大写)指定库文件所在目录
    # -L参数跟着的是库文件所在的目录名
   # case: 链接mytest库，libmytest.so在/home/bing/mytestlibfolder目录下
   g++ -L/home/bing/mytestlibfolder -lmytest test.cpp
   ```

4. -I --- 指定头文件搜索目录（大写的i）

   ```shell
   # /usr/include目录一般是不用指定的，gcc知道去那里找，但是如果头文件不在/usr/icnclude里我们就要用-I参数指定了，比如头文件放在/myinclude目录里，那编译命令行就要加上-I/myinclude 参数了，如果不加你会得到一个”xxxx.h: No such file or directory”的错误。-I参数可以用相对路径，比如头文件在当前目录，可以用-I.来指定。上面我们提到的–cflags参数就是用来生成-I参数的
   g++ -I/myinclude test.cpp
   ```

5. -Wall --- 打印警告信息

   ```shell
   # 打印出gcc提供的警告信息
   g++ -Wall test.cpp
   ```

6. -W --- 关闭警告信息

   ```shell
   # 关闭所有的警告信息
   g++ -W test.cpp
   ```

7. -std=c++11 --- 设置编译标准

   ```shell
   # 使用c++11标准编译test.cpp
   g++ -std=c++11 test.cpp
   ```

8. -o --- 指定输出文件名

   ```shell
   # 指定即将产生的文件名
   # 如果不指定文件名，编译器将默认输出 a.out 的可执行文件
   g++ test.cpp -o test
   ```

9. -D --- 定义宏

   ```c++
   /*
       在使用gcc/g++编译的时候定义宏
       常用场景：
       -DDEBUG 定义DEBUG宏，可能文件中有DEBUG宏部分的相关信息，用个DDEBUG来选择开启或关闭DEBUG
   */
   
    // -Dname 定义宏name,默认定义内容为字符串“1”
    #include <stdio.h>
   
    int main()
    {
        #ifdef DEBUG
            printf("DEBUG LOG\n");
        #endif
           printf("in\n");
   }
   
   // 1. 在编译的时候，使用gcc -DDEBUG main.cpp
   // 2.  此时 printf("DEBUG LOG\n") 可以被执行
   ```

   

#### 3.3 实战 --- g++命令行编译

- **库文件**：库文件是事先编译好的方法的合集。比如：我们提前写好一些数据公式的实现，将其打包成库文件，以后使用只需要库文件就可以，不需要重新编写。
- Linux系统中
  - **静态库**的扩展名为 .a，编译时用
  - **动态库**的扩展名为 .so，运行时用

```shell
# 最初目录结构
.
├── include
│               └── Swap.h
├── main.cpp
└── src
                └── Swap.cpp

2 directories, 3 files
```

- **直接编译**

  ```shell
  # 将 main.cpp 和 Swap.cpp 编译为可执行文件
  g++ main.cpp src/Swap.cpp -Iinclude  # -I 为指定所包含的头文件所在目录
  # 运行 a.out
  ./a.out
  ```

- **增加参数编译**

  ```shell
  # 将 main.cpp src/Swap.cpp 编译为可执行文件 附带一堆参数
  g++ main.cpp src/Swap.cpp -Iinclude -std=c++11 -O2 -Wall -o b.out
  # 运行 b.out
  ./b.out
  ```

- **生成静态库文件并编译**

  ```shell
  # 将 Swap.cpp 文件生成一个静态库，然后链接到 main.cpp 中并生成一个可执行文件
  # 1. 进入src目录下(Swap.cpp所在目录)
  cd src 
  
  # 2. 生成二进制文件
      # -c：生成.o的二进制文件
      # -I：指定头文件所在的目录
      # ../：上级目录
  g++  Swap.cpp  -c -I../include  
  
  # 3. 归档生成静态库 libSwap.a
  ar  rs  libSwap.a  Swap.o
  
  # 4. 链接到 main.cpp 并生成一个可执行文件static_main
  	# ..：上级目录
  	# -lSwap：指定链接的库文件为 libSwap
  	# -Lsrc：指定库文件所在的路径
  	# -Iinclude：指定头文件的搜索目录
  	# -o：指定可执行文件的文件名
  cd ..
  g++  main.cpp  -lSwap -Lsrc -Iinclude -o static_main
  
  # 5. 运行可执行文件
  ./static_main
  ```

- **生成动态库文件并编译**

  ```shell
  # 将 Swap.cpp 文件生成一个动态库，然后链接到 main.cpp 中并生成一个可执行文件
  # 1. 进入src目录下(Swap.cpp所在目录)
  cd src 
  
  # 2. 生成动态库 libSwap.so
  	# -I../include：指定头文件的搜索目录
  	# -fPIC：代表与路径无关
  	# -shared：代表生成的是动态库文件
  	# -o：指定动态库文件名
  g++ Swap.cpp -I../include -fPIC -shared -o libSwap.so
  	# 上面命令等价于以下两条命令
      # gcc Swap.cpp -I../include -c -fPIC （生成二进制文件）
      # gcc -shared -o libSwap.so Swap.o（生成动态库）
      
  # 3. 链接到 main.cpp 并生成一个可执行文件shared_main
  	# -lSwap：指定链接的库文件为 libSwap
  	# -Lsrc：指定库文件所在的路径
  	# -Iinclude：指定头文件的搜索目录
  	# -o：指定可执行文件的文件名
  cd ..
  g++ main.cpp -lSwap -Iinclude -Lsrc -o shared_main
  
  # 4. 运行可执行文件
  LD_LIBRARY_PATH=src ./shared_main
  ```

  

### 四、GDB调试器

- **GDB** (GNU Debugger) 是一个用来**调试C/C++程序**的功能强大的**调试器**，是Linux系统开发C/C++最常用的调试器
- 程序员可以**使用GDB来跟踪程序中的错误**，从而减少程序员的工作量
- **VSCode是通过调用GDB调试器来实现C/C++的调试工作的**

- **GDB主要功能：**
  - 设置**断点**(断点可以是条件表达式)
  - 使程序在指定的代码行上暂停执行，便于观察
  - **单步**执行程序，便于调试
  - 查看程序中变量值的变化
  - 动态改变程序的执行环境
  - 分析崩溃程序产生的core文件



#### 4.1 常用的调试命令参数

**Tips:**

1. 编译程序时需要加上-g，之后才能用gdb进行调试：`gcc -g main.c -o main`
2. 回车键：重复上一命令

- **进入调试程序**

  ```shell
  gdb [exefilename]  ---  进入gdb调试程序，exefilename为可执行文件名
  ```

- **常用调试命令**

  ```shell
  # 以下命令后括号内为命令的简化使用，比如run（r），直接输入命令 r 就代表命令run
  help(h)        # 查看命令帮助，具体命令查询在gdb中输入help + 命令 
  run(r)         # 重新开始运行文件（run-text：加载文本文件，run-bin：加载二进制文件）
  start          # 单步执行，运行程序，停在第一行执行语句
  list(l)        # 查看原代码（list-n,从第n行开始查看代码。list+ 函数名：查看具体函数）
  set            # 设置变量的值
  next(n)        # 单步调试（逐过程，函数直接执行）
  step(s)        # 单步调试（逐语句：跳入自定义函数内部执行）
  backtrace(bt)  # 查看函数的调用的栈帧和层级关系
  frame(f)       # 切换函数的栈帧
  info(i)        # 查看函数内部局部变量的数值
  finish         # 结束当前函数，返回到函数调用点
  continue(c)    # 继续运行
  print(p)       # 打印值及地址
  quit(q)        # 退出gdb
  break+num(b)                 # 在第num行设置断点
  info breakpoints             # 查看当前设置的所有断点
  delete breakpoints num(d)    # 删除第num个断点
  display                      # 追踪查看具体变量值
  undisplay                    # 取消追踪观察变量
  watch                        # 被设置观察点的变量发生修改时，打印显示
  i watch                      # 显示观察点
  enable breakpoints           # 启用断点
  disable breakpoints          # 禁用断点
  x                            # 查看内存x/20xw 显示20个单元，16进制，4字节每单元
  run argv[1] argv[2]          # 调试时命令行传参
  set follow-fork-mode child   # Makefile项目管理：选择跟踪父子进程（fork()）
  ```




### 五、IDE-VSCode

#### 5.1 **常用快捷键**

<img src="https://mmbiz.qpic.cn/mmbiz_png/NSZJKGNrtpdRPOo8IDpFUJMUmmZWd6prBa0nIu1uDUSlMaIWPvhDhJJ1NTncQRx8hAHa0OMokLFW5cySFfVEOg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" style="zoom:67%;" />

**在 `Ctrl+P` 窗口下还可以:**

- 直接输入文件名，跳转到文件		

- `?` 列出当前可执行的动作

- `!` 显示 `Errors`或 `Warnings`，也可以 `Ctrl+Shift+M`

- `:` 跳转到行数，也可以 `Ctrl+G` 直接进入

- `@` 跳转到 `symbol`（搜索变量或者函数），也可以 `Ctrl+Shift+O` 直接进入

- `@` 根据分类跳转 `symbol`，查找属性或函数，也可以 `Ctrl+Shift+O` 后输入:进入

- `#` 根据名字查找 `symbol`，也可以 `Ctrl+T`

  

- **快捷键：编辑器与窗口管理**

  1. 打开一个新窗口：`Ctrl+Shift+N`
  2. 关闭窗口：`Ctrl+Shift+W`
  3. 同时打开多个编辑器（查看多个文件）
  4. 新建文件 `Ctrl+N`
  5. 文件之间切换 `Ctrl+Tab`
  6. 切出一个新的编辑器（最多 `3` 个） `Ctrl+\`，也可以按住 `Ctrl` 鼠标点击 `Explorer` 里的文件名
  7. 左中右 `3` 个编辑器的快捷键 `Ctrl+1` `Ctrl+2` `Ctrl+3`

  8. 编辑器换位置， `Ctrl+k`然后按 `Left`或 `Right`

     

- **↓ 代码编辑相关的快捷键 ↓**

- **快捷键：格式调整**

  1. 代码行缩进 `Ctrl+[` 、 `Ctrl+]`
  2. `Ctrl+C` 、 `Ctrl+V` 复制或剪切当前行/当前选中内容
  3. 代码格式化：`Shift+Alt+F`，或 `Ctrl+Shift+P` 后输入 `format code`
  4. 上下移动一行：`Alt+Up` 或 `Alt+Down`
  5. 向上向下复制一行：`Shift+Alt+Up` 或 `Shift+Alt+Down`
  6. 在当前行下边插入一行 `Ctrl+Enter`
  7. 在当前行上方插入一行 `Ctrl+Shift+Enter`

  

- **快捷键：光标相关**

  1. 移动到行首：`Home`
  2. 移动到行尾：`End`
  3. 移动到文件结尾：`Ctrl+End`
  4. 移动到文件开头：`Ctrl+Home`
  5. 移动到定义处：`F12`
  6. 定义处缩略图：只看一眼而不跳转过去 `Alt+F12`
  7. 移动到后半个括号：`Ctrl+Shift+]`
  8. 选择从光标到行尾：`Shift+End`
  9. 选择从行首到光标处：`Shift+Home`
  10. 删除光标右侧的所有字：`Ctrl+Delete`
  11. 扩展/缩小选取范围：`Shift+Alt+Left` 和 `Shift+Alt+Right`
  12. 多行编辑(列编辑)：`Alt+Shift+鼠标左键`，`Ctrl+Alt+Down/Up`
  13. 同时选中所有匹配：`Ctrl+Shift+L`

  14. `Ctrl+D` 下一个匹配的也被选中 (在 sublime 中是删除当前行，后面自定义快键键中，设置与 `Ctrl+Shift+K` 互换了)
  15. 回退上一个光标操作：`Ctrl+U`

  

- **快捷键：重构代码**

  1. 找到所有的引用：`Shift+F12`
  2. 同时修改本文件中所有匹配的：`Ctrl+F12`
  3. 重命名：比如要修改一个方法名，可以选中后按 `F2`，输入新的名字，回车，会发现所有的文件都修改了
  4. 跳转到下一个 `Error` 或 `Warning`：当有多个错误时可以按 `F8` 逐个跳转
  5. 查看 `diff`：在 `explorer` 里选择文件右键 `Set file to compare`，然后需要对比的文件上右键选择 `Compare with file_name_you_chose`

  

- **快捷键：查找替换**
  1. 查找 `Ctrl+F`
  2. 查找替换 `Ctrl+H`
  3. 整个文件夹中查找 `Ctrl+Shift+F`



- **快捷键：显示相关**
  1. 全屏：`F11`
  2. zoomIn/zoomOut：`Ctrl +/-`
  3. 侧边栏显/隐：`Ctrl+B`
  4. 显示资源管理器 `Ctrl+Shift+E`
  5. 显示搜索 `Ctrl+Shift+F`
  6. 显示 Git `Ctrl+Shift+G`
  7. 显示 Debug `Ctrl+Shift+D`
  8. 显示 Output `Ctrl+Shift+U`



### 六、CMake

- **CMake**是一个**跨平台**的安装**编译工具**，可以用**简单**的语句来描述**所有平台**的安装（编译过程）
- CMake可以说成为**C++开源项目的标准**

#### 6.1 跨平台开发

- **不使用CMake**

  假设您有一些跨平台项目，其中 C++ 代码在不同平台/IDE 上共享。假设您`Visual Studio`在 Windows、`Xcode`OSX 和`Makefile`Linux 上使用：

  <img src="https://mmbiz.qpic.cn/mmbiz_png/NSZJKGNrtpdRPOo8IDpFUJMUmmZWd6prSrUvfw5dhVGhiafp4eM7ybic5A4orkha8Gicpp4sHJpYeKcVdiboq4iahNQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" style="zoom:80%;" />

  如果你想添加新的`bar.cpp`源文件，你会怎么做？您必须将其添加到您使用的每个工具中：

  <img src="https://mmbiz.qpic.cn/mmbiz_png/NSZJKGNrtpdRPOo8IDpFUJMUmmZWd6prDDI4x578KmXwN3RqlG8lMY6KwibmT5DGiaF4sf51vib0wBLbYia4AMsuIQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" style="zoom:80%;" />

  为了保持环境一致，您必须多次进行类似的更新。最重要的是您必须**手动完成**（在这种情况下，图中用红色标记的箭头）。当然，这种方法容易出错且不灵活。

- **使用CMake**

  CMake 通过在开发过程中增加额外的步骤来解决这个设计缺陷。您可以在文件中描述您的项目，`CMakeLists.txt`并使用 CMake 生成您当前对使用跨平台 CMake 代码感兴趣的工具：

  <img src="https://mmbiz.qpic.cn/mmbiz_png/NSZJKGNrtpdRPOo8IDpFUJMUmmZWd6pr8QNE00hTL0pficiaBlntnkQTC46U7woqtrnMbibXLnKZsUAvNmXaaYNiaQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" style="zoom:80%;" />

  相同的操作 - 添加新`bar.cpp`文件，现在将**一步完成**：

  <img src="https://mmbiz.qpic.cn/mmbiz_png/NSZJKGNrtpdRPOo8IDpFUJMUmmZWd6pr56U8Xicjw7Be5K6ETmPiaG8X5CX4LkQJ4UXVc6FfMQJ7QtUttu6d0d5A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" style="zoom:80%;" />

  注意图表的底部没有**改变**。即你仍然可以继续使用你最喜欢的工具，比如`Visual Studio/msbuild`，`Xcode/xcodebuild`和`Makefile/make`！



#### 6.2 CMake语法特性介绍

- **基本语法格式：指令(参数1 参数2…)**

  - 参数使用**括弧**括起
  - 参数之间使用**空格**或**分号**隔开

- **CMake指令是大小写无关的，但其使用的参数和变量是大小写相关的**

  ```cmake
  set(HELLO  hello.cpp)
  add_executable(hello main.cpp  hello.cpp)
  ADD_EXECUTABLE(hello  main.cpp ${HELLO})
  ```

- **变量使用${}方式取值，但是在 IF 控制语句中是直接使用变量名(不用加${})**



#### 6.3 重要指令和CMake常用变量

##### 6.3.1 重要指令 （[]内为可选项）

- **cmake_minimum_required**  ---  指定CMake的最小版本要求

  - 语法：cmake_minumum_required(VERSION  versionNumber  [FATAL_ERROR])

    ```cmake
    # CMake的最小版本要求为2.8.3
    cmake_minimum_required(VERSION  2.8.3)
    ```

  

- **project**  ---  定义工程名称，指定工程支持的语言

  - 语法：project(projectName  \[CXX] \[C] [Java])

    ```cmake
    # 指定工程名为HELLOWORLD
    project(HELLOWORLD)
    ```

  

- **set**  ---  显式地定义变量

  - 语法：set(VAR  [VALUE] [CACHE TYPE DOCSTRING  [FORCE]])

    ```cmake
    # 定义SRC变量，其值为main.cpp hello.cpp
    set(SRC  sayhello.cpp  hello.cpp)
    ```

  

- **include_directories**  ---  向工程添加特定的头文件搜索路径（相当于指定g++编译器的-I参数）

  - 语法：include_directories([AFTER|BEFORE] [SYSTEM] dir1 dir2 …)

    ```cmake
    # 将/usr/include/myincludefolder (绝对路径) 和 ./include (相对路径) 添加到头文件搜索路径
    include_directories(/usr/include/myincludefolder  ./include)
    ```

  

- **link_directories**  ---  向工程添加特定的库文件搜索路径 (相当于指定g++编译器的-L参数)

  - 语法：link_directories(dir1 dir2 …) 

    ```cmake
    # 将/usr/lib/mylibfolder 和 ./lib 添加到库文件搜索路径
    link_directories(/usr/lib/mylibfolder  ./lib)
    ```

  

- **add_library**  ---  生成库文件

  - 语法：add_library(libname [SHARED|STATIC|MODULE] [EXCLUDE_FROM_ALL] source1 source2 … sourceN)

    ```cmake
    # 通过变量 SRC 生成 libhello.so 共享库
    add_library(hello  SHARED ${SRC})
    ```

  

- **add_compile_options**  ---  添加编译参数

  - 语法：add_compile_options(<option>  ...)

    ```cmake
    # 添加编译参数 -Wall -std=c++11  -O2
    add_compile_options(-Wall  -std=c++11  -O2)
    ```

  

- **add_executable**  ---  生成可执行文件

  - 语法：add_executable(exeName  source1  source2  ...  sourceN)

    ```cmake
    # 编译main.cpp生成可执行文件main
    add_executable(main  main.cpp)
    ```

  

- **target_link_libraries**  ---  为目标添加需要链接的共享参数库（相当于指定g++编译器-l参数）

  - 语法：target_link_libraries(target  library1<debug | optimized> library2  ...)

    ```cmake
    # 将hello动态库文件链接到可执行文件main
    target_link_libraries(main  hello)
    ```

  

- **add_subdirectory**  ---  向当前工程添加存放源文件的子目录，并可以指定中间二进制和目标二进制存放的位置

  - 语法：add_subdirectory(source_dir  [binary_dir]  [EXCLUDE_FROM_ALL])

    ```cmake
    # 添加src子目录，src中需要有一个CMakeLists.txt
    add_subdirectory(src)
    ```

    

- **aux_source_directory**  ---  发现一个目录下所有的源代码文件，并将文件列表存储在一个变量中，这个指令临时被用来自动构建源文件列表

  - 语法：aux_source_directory(dir  VARIABLE)

    ```cmake
    # 定义SRC变量，其值为当前目录下所有的源代码文件
    aux_source_directory(.  SRC)  # .代表当前目录
    # 编译SRC变量所代表的源代码文件，生成main可执行文件
    add_executable(main  ${SRC})
    ```



##### 6.3.2 CMake常用变量

- **CMAKE_C_FLAGS gcc编译选项**   &&  **CMAKE_CXX_FLAGS g++编译选项**

  ```cmake
  # 在CMAKE_CXX_FLAGS编译选项后追加-std=c++11
  set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS}  -std=c++11")
  ```



- **CMAKE_BUILD_TYPE 编译类型(Debug, Release)**

  ```cmake
  # 设定编译类型为debug，调试时需要选择debug
  set(CMAKE_BUILD_TYPE  Debug)
  # 设定编译类型为release，发布时需要选择release
  set(CMAKE_BUILD_TYPE  Release)
  ```



- **CMAKE_BINARY_DIR**  &&  **PROJECT_BINARY_DIR**  &&  **<项目名称>__BINARY_DIR**
  1. 这三个变量指代的内容是一致的。
  2. 如果是在源码构建中，指的就是工程目录。
  3. 如果是out-of-source编译，指的是工程编译发生的目录。
  4. PROJECT_BINARY_DIR 跟其他指令有点不同，不过现在，你可以理解为他们是一致的。



- **CMAKE_SOURCE_DIR**  &&  **PROJECT_SOURCE_DIR**  &&  **<项目名称>__SOURCE_DIR**
  1. 三个变量的内容是一致的，不管是采用哪种方式，都指代工程目录。
  2. 也是在源码编译的时候，他跟CMAKE_BINARY_DIR等变量一致。
  3. PROJECT_SOURCE_DIR 跟其他指令有点不同，现在，你可以理解为他们是一致的。



- **CMAKE_C_COMPILER**：指定C编译器
- **CMAKE_CXX_COMPILER**：指定C++编译器
- **EXOUTPUT_PATH**：文件输出的ECU路径
- **LIBRARY_OUTPUT**：库文件输出的存放路径



#### 6.4 CMake编译工程

- CMake目录结构：项目主目录存在一个CMakeLists.txt文件
- **方式设置集合规则**：
  1. 包含源文件的子文件夹包含CMakeLists.txt文件，主的CMakeLists.txt通过add_subdirectory添加子目录即可
  2. 包含源文件的文件夹未包含CMakeLists.txt文件，子目录编译中主流主流在主目录的CMakeLists.txt

-  **编译流程**

  在 linux 平台下使用 CMake 制作 C/C++ 工程的流程如下：

  - 手动编写CmakeLists.txt。

  - 执行命令`cmake PATH`生成生成CMakeLists.txt的目录。

  - 执行命令`make`进行编译。

- **两种构建方式**

  - **内部构建**（in-source build）：不推荐使用

    内部构建会在同级目录下产生一大堆中间文件，这些中间文件并不是我们最终所需要的，和工程源文件放在一起会显得杂乱无章

    ```shell
    ## 内部构建
    # 1. 在当前目录下，编译本目录的CMakeLists.txt，生成Makefile和其他文件
    cmake .
    # 2. 执行make命令，生成target
    make
    ```

  - **外部构建**（out-of_source build）：推荐使用

    将编译输出的文件与源文件放在不同的目录中

    ```shell
    ## 外部构建
    # 1. 在当前目录下，创建build文件夹
    mkdir build 
    # 2. 进入到build文件夹
    cd build
    # 3. 编译上级目录的CMakeLists.txt，生成Makefile和其他文件
    cmake ..
    # 4. 执行make命令，生成target
    make
    ```



#### 6.5 CMake代码实践

```cmake
cmake_minimum_required(VERSION 3.0)

project(SWAP)

include_directories(include)

add_executable(main_cmake main.cpp src/swap.cpp)
```



















































