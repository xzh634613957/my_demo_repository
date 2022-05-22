### Linux常用命令

**cd**             <u>至家目录/home/username</u>

cd ~          <u>至家目录/home/username</u>

cd + *目录名*			  <u>至某一目录</u>

cd -			<u>至上次访问的目录</u>

cd ..           <u>返回上一目录</u>

**touch**       <u>创建空文件</u>

touch .*file_name*  <u>创建隐藏文件</u>

**mkdir**		<u>创建空文件夹</u>

**mkdir -p**    <u>递归创建目录</u>

**cat** *file_name*      <u>查看文件内容（文件内容少的时候使用）</u>

cat -b *file_name*   <u>查看文件时同时对非空行进行编号</u>

cat -n *file_name*    <u>查看文件的同时对所有行进行编号</u>

**more** *file_name*   <u>查看文件内容</u>（文件内容多的时候使用，会分屏显示）

**gedit**         <u>创建文件并编辑</u>

**grep**   *搜索内容*  *文件名*      <u>在文件中搜索指定内容</u>（Ctrl + F）

grep -n     <u>显示匹配行及行号</u>

grep -i       <u>忽略大小写</u>

grep ^a     <u>搜索以a开头的行</u>

grep a$     <u>搜索以a结尾的行</u>  

**rm**             <u>删除文件</u>（使用rm删除文件后无法恢复）

rm -r         <u>删除文件夹</u>

rm -f         <u>强制删除，忽略不存在的文件，无需提示</u>

**ls**              <u>显示当前的文件夹目录</u>

ls -a          <u>显示当前包括隐藏文件的文件夹目录</u>

ls -lh       <u>以列表的形式显示文件的详细信息</u>

**cp** *file_name* Desktop/    <u>复制文件至桌面</u>

cp -i  *file_name* Desktop/  <u>覆盖文件前提示</u>

cp -r                                     <u>复制文件夹</u>

**mv**  *file_name*  *文件目录*  <u>移动文件至某一文档</u>（也可以用来重命名）

mv -i  *file_name*  Desktop/  <u>覆盖文件前提示</u>

**echo**     <u>输出后面的文字内容，通常与>和>>一起使用（相当于print）</u>

**>**  *file_name*    <u>重定向，将会显示在终端的内容输出到指定文件中，会覆盖原有的内容</u>

**>>**  *file_name*   <u>重定向，将会显示在终端的内容追加到指定文件的末尾，不会覆盖原有的内容</u>  

*命令1* **|** *命令2*         <u>管道，将前一个命令的输出当作下一个命令的输入，可与grep连用</u>

**vi** + 文件名       <u>打开文件</u>

**tree**    <u>以树状图的形式列出当前目录及目录下的目录和文件的结构</u>

tree -d   <u>以树状图的形式列出当前目录及目录下的目录的结构</u>

**clear**        <u>清屏</u>

ifconfig   <u>查看/配置计算机当前的网卡配置信息及IP地址</u>

ping  *IP地址*   <u>检测到目标主机是否连接正常</u>

ping 127.0.0.1    <u>检测本地网卡是否工作正常</u>

![image-20211129205647295](/home/xiongzh/文档/Ubuntu_Linux常用操作/Ubuntu_Linux常用操作.assets/image-20211129205647295-16381906120731.png)

### 查看系统信息

**df -h**       <u>查看磁盘空间</u>

**du -h**      <u>查看当前目录下的文件大小</u>

date         <u>查看系统时间</u>

cal             <u>查看当前月日历</u>

cal -y         <u>查看一年的日历</u>

ps au        <u>查看进程的详细情况</u>

**top**           <u>动态显示运行中的进程并排序（按q退出）</u>

**htop**          <u>动态显示运行中的进程并排序（按q退出）</u>

kill -9 *进程代号*   <u>强行终止指定代号(PID)的进行</u>

### 权限

**sudo su**   <u>root超级用户权限</u>

exit           <u>退出root用户</u>

**chmod +/- rwx**    <u>修改文件权限</u>

chown      <u>修改文件拥有者</u>

chgrp        <u>修改组</u>

### Terminator终端快捷键

**Ctrl + alt + t**    <u>打开终端</u>

**Ctrl + Shift + o**       <u>水平分割终端（分成上下两个窗口）</u>

**Ctrl + Shift + e**       <u>垂直分割终端（分成左右两个窗口）</u>

**Ctrl + Shift + w**       <u>关闭当前终端</u>

Ctrl + Shift + q        <u>关闭所有终端（退出程序)</u>

**Ctrl + Shift + x**        <u>放大（还原）当前终端</u>

Ctrl+ Shift + g       <u>清屏（全清）</u>

Ctrl + l                   <u>清屏（留最新一行）</u>

Ctrl + Tab             <u>在不同的工作区间循环</u>

Ctrl + p                 <u>在不同的工作区间循环</u>

**Alt + 上/下/左/右**           <u>在不同的工作区间移动</u>

Ctrl + Shift + 左/右          <u>在垂直分割的终端中将分割条向左/右移动</u>

Ctrl + Shift + 上/下           <u>在垂直分割的终端中将分割条向上/下移动</u>

Ctrl + Shift + s                  <u>隐藏/显示滚动条</u>

F11                                 <u>全屏/退出全屏</u>

Ctrl + Shift + =                  <u> 放大终端窗口的字体显示</u>

Ctrl + -                             <u>缩小终端窗口的字体显示</u>

**Ctrl + c**                            <u>退出当前命令</u>

### 常用快捷键

alt + F2           <u>运行命令</u>

tab                  <u>自动补齐</u>

ctrl + h           <u>显示隐藏文件</u>

### VIM编辑常用命令

:wq          <u>保存并退出</u>

:q!            <u>强制退出且不保存</u>

u              <u>撤销上一步</u>

i                <u>编辑输入</u>

Esc键            <u>退出编辑</u>

### 安装/卸载/更新软件

sudo apt install *package*         <u>安装包</u>

sudo apt remove *package*      <u>删除包</u>

sudo apt upgrade                   <u>更新已安装的包</u>

sudo apt update                       <u>更新软件源和软件列表</u>

apt-cache search *package*             <u>搜索包</u>

apt-cache show *package*               <u>获取包的相关信息</u>

sudo  dpkg  -i  deb文件名    <u>安装deb程序文件</u>

### 压缩/解压缩

**tar -zcvf**  *打包文件.tar.gz 被压缩的文件/路径*　<u>压缩文件（多个文件用空格隔开）</u>

**tar -jcvf**   *打包文件.tar.bz2  被压缩的文件/路径*　<u>压缩文件（多个文件用空格隔开）</u>

**tar -zxvf ** *打包文件.tar.gz*                                     <u>解压文件</u>

**tar -jxvf**  *打包文件.tar.bz2*                                    <u>解压文件</u>

**tar -Jxvf**  *打包文件.tar.xz*                                    <u>解压文件</u>

**tar -zxvf**  *打包文件.tar.gz -C 目标路径*                <u>解压文件至指定路径</u>

**tar -jxvf**  *打包文件.tar.bz2 -C 目标路径*                <u>解压文件至指定路径</u>

### 命令行

gnome-tweaks        <u>优化窗口</u>

### 软件

./cfw                               <u>执行Clash for Windows（科学上网）</u>

./RUN-ME.sh                 <u>执行迷雾通</u>

sudo sysmontask        <u>运行任务管理器</u> 

flameshot gui            <u>截图（Ctrl + Alt + A）</u>

### 通配符

"*"  <u>代表任意个数的字符</u>

？    <u>代表任意一个字符</u>

[123]  <u>表示可以匹配字符组123中的任意一个</u>

[abc]    <u>匹配abc中的任意一个</u>

[a-f]      <u>匹配从a到f的范围内的任意一个字符</u>
