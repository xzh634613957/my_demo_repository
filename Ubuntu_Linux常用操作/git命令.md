### git命令

- **初始配置**

  ```shell
   # 1.安装
   $ sudo apt-get install git
   
   # 2.用户名登陆
   # --global参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置
   $ git config --global user.name "Your Name"
   $ git config --global user.email "you@example.com"
  ```

- **创建版本库(仓库-repository)**

  ```shell
  # 1.选择一个合适的地方，创建一个空目录
  $ mkdir ~/my_work
  $ cd my_work
  
  # 2.通过git init命令把这个目录变成Git可以管理的仓库
  $ git init
  ```

- **将文件推到git**

  ```shell
   # 1.把文件添加到仓库(在仓库目录下的文件)
   # 可反复多次使用，添加多个文件
   $ git add readme.txt
   # 直接添加当前目录
   $ git add .
   
   # 2.把文件提交到仓库
   # -m后面输入的是本次提交的说明，可以输入任意内容
   $ git commit -m "wrote a readme file"
  ```

- **版本回退**

  ```shell
   # 1.当仓库中的文件有修改时，git status命令可以让我们时刻掌握仓库当前的状态
   $ git status
   # 有修改未提交时的输出（当前有需要提交的修改）：
      On branch master
      Changes not staged for commit:
        (use "git add <file>..." to update what will be committed)
        (use "git checkout -- <file>..." to discard changes in working directory)
  
          modified:   README.md
  
      no changes added to commit (use "git add" and/or "git commit -a")
   # 有修改提交后未说明时的输出（当前有需要提交的更改说明）：
       On branch master
      nothing to commit, working tree clean
       On branch master
      Changes to be committed:
        (use "git reset HEAD <file>..." to unstage)
  
          modified:   README.md
    # 有修改提交并说明后的输出（当前没有需要提交的修改）：
        On branch master
      nothing to commit, working tree clean
  
   # 2.git diff查看具体修改的内容
   $ git diff
       diff --git a/README.md b/README.md
      index 7e58a0f..aa72a68 100644
      --- a/README.md
      +++ b/README.md
      @@ -1,3 +1,5 @@
       该仓库存放一些demo文件。
  
      -This repository stores some demo files.
      \ No newline at end of file
      +This repository stores some demo files.
      +
      +是否修改？
      \ No newline at end of file
  
  # 3.git log显示从最近到最远的提交日志
  # HEAD表示当前版本，也就是最新的提交
  $ git log
      commit 18051e599b2da7b765130c06ea77b3fa7ba75152 (HEAD -> master)
      Author: xzh634613957 <xzh191194@163.com>
      Date:   Sat May 21 11:46:08 2022 +0800
  
          版本回溯
  
      commit eddeef8bc0b7c10d06ccf33ac5e0efa6ffaa2060
      Author: xzh634613957 <xzh191194@163.com>
      Date:   Sat May 21 11:34:10 2022 +0800
  
          是否修改？
  
      commit 7a2effaa0aa0d8741a08319ccd36103760eeefa6
      Author: xzh634613957 <xzh191194@163.com>
      Date:   Sat May 21 11:12:56 2022 +0800
  
          add a readme file
  # 如果嫌输出信息太多，可以试试加上--pretty=oneline参数
  # 前面的一串字符是commit id（版本号），后面的是提交的日志信息
  $ git log --pretty=oneline
      18051e599b2da7b765130c06ea77b3fa7ba75152 (HEAD -> master) 版本回溯
      eddeef8bc0b7c10d06ccf33ac5e0efa6ffaa2060 是否修改？
      7a2effaa0aa0d8741a08319ccd36103760eeefa6 add a readme file
  
  # 4.版本回溯
  # 要把当前版本回退到上一个版本，可以使用git reset命令
  # 首先，Git必须知道当前版本是哪个版本，在Git中，用HEAD表示当前版本，也就是最新的提交，上一个版本就是HEAD^，上上一个版本就是HEAD^^，当然往上100个版本写100个^比较容易数不过来，所以写成HEAD~100
  $ git reset --hard HEAD^
  	HEAD is now at eddeef8 是否修改？
  # 恢复新版本的方法：git reflog找到新版本的commit id，再使用git reset --hard ${commit_id}
  # 版本号没必要写全，前几位就可以了，Git会自动去找
  $ git reflog
      eddeef8 (HEAD -> master) HEAD@{0}: reset: moving to HEAD^
      18051e5 HEAD@{1}: commit: 版本回溯
      eddeef8 (HEAD -> master) HEAD@{2}: commit: 是否修改？
      7a2effa HEAD@{3}: commit (initial): add a readme file
  $ git reset --hard 18051
  	HEAD is now at 18051e5 版本回溯
  
  # 5.总结
      HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id。
      穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。
      要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。
  ```

- **工作区和暂存区**

  ```shell
  # 工作区（Working Directory）：就是在电脑里能看到的目录
  # 版本库（Repository）：工作区有一个隐藏目录.git，这个不算工作区，而是Git的版本库
  # 暂存区：Git的版本库里存了很多东西，其中最重要的就是称为stage（或者叫index）的暂存区，还有Git为我们			自动创建的第一个分支master，以及指向master的一个指针叫HEAD
  # 第一步是用git add把文件添加进去，实际上就是把文件修改添加到暂存区
  # 第二步是用git commit提交更改，实际上就是把暂存区的所有内容提交到当前分支
  # 每次修改，如果不用git add到暂存区，那就不会加入到commit中
  ```

  ![git-repo](https://www.liaoxuefeng.com/files/attachments/919020037470528/0)

- **撤销修改**

  ```shell
  # git checkout -- file 可以丢弃工作区的修改
  # 命令git checkout -- readme.txt意思就是，把readme.txt文件在工作区的修改全部撤销，这里有两种情	况：
  # 一种是readme.txt自修改后还没有被放到暂存区(还没git add)，现在，撤销修改就回到和版本库一模一样的状态(回到最近一次git commit)
  # 一种是readme.txt已经添加到暂存区后(已经git add，还没git commit)，又作了修改，现在，撤销修改就回到添加到暂存区后的状态(回到最近一次git add)
  # 总之，就是让这个文件回到最近一次git commit或git add时的状态
  # git checkout -- file命令中的--很重要，没有--，就变成了“切换到另一个分支”的命令
  # git checkout -- file其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”
  
  # 对于第一种情况，没有被放到暂存区(还没git add)
  $ git checkout -- README.md
  
  # 对于第二种情况，git add到暂存区了(还没git commit)
  # 用命令git reset HEAD <file>可以把暂存区的修改撤销掉（unstage），重新放回工作区，再使用checkout丢弃工作区的修改
  $ git reset HEAD README.md
      Unstaged changes after reset:
      M	README.md
  $ git checkout -- README.md
  
  # 总结：
  场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file。
  场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD <file>，就回到了场景1，第二步按场景1操作。
  场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。
  ```

- **删除文件**

  ```shell
  # 一般情况下，你通常直接在文件管理器中把没用的文件删了，或者用rm命令删了
  $ rm test.txt
  $ git status
      On branch master
      Changes not staged for commit:
        (use "git add/rm <file>..." to update what will be committed)
        (use "git checkout -- <file>..." to discard changes in working directory)
  
          deleted:    test.txt
  
      no changes added to commit (use "git add" and/or "git commit -a")
  # 现在你有两个选择，一是确实要从版本库中删除该文件，那就用命令git rm删掉，并且git commit
  $ git rm test.txt 
  	rm 'test.txt'
  $ git commit -m "remove test.txt"
      [master cdcd32e] remove test.txt
       1 file changed, 0 insertions(+), 0 deletions(-)
       delete mode 100644 test.txt
  # 另一种情况是删错了，因为版本库里还有呢，所以可以很轻松地把误删的文件恢复到最新版本：
  $ git checkout -- test.txt
  ```

- **远程仓库SSH密匙配置**

  https://www.liaoxuefeng.com/wiki/896043488029600/896954117292416

  ```shell
  # 1.本地Git仓库和GitHub仓库之间的传输是通过SSH加密的，所以，需要一点设置：
  $ ssh-keygen -t rsa -C "youremail@example.com"
  # 2.然后一路回车，使用默认值即可
  # 3.在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件，这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人
  # 4.登陆GitHub，打开“settings”，“SSH and GPG Keys”页面，点“New SSH Key”，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容
  # 5.为什么GitHub需要SSH Key呢？因为GitHub需要识别出你推送的提交确实是你推送的，而不是别人冒充的，而Git支持SSH协议，所以，GitHub只要知道了你的公钥，就可以确认只有你自己才能推送。
  # 6.GitHub允许你添加多个Key。假定你有若干电脑，你一会儿在公司提交，一会儿在家里提交，只要把每台电脑的Key都添加到GitHub，就可以在每台电脑上往GitHub推送了
  ```

- **添加远程仓库**

  ```shell
  # 在本地创建了一个Git仓库后，又想在GitHub创建一个Git仓库，并且让这两个仓库进行远程同步，这样，GitHub上的仓库既可以作为备份，又可以让其他人通过该仓库来协作
  # 1.登陆GitHub，点击"New"创建一个新的仓库
  
  # 2.在Repository name填入仓库名称，其余保持默认即可
  
  # 3.将本地仓库推送至GitHub(也可以采用其他方式，从这个仓库克隆出新的仓库)，在本地仓库下运行命令,添加后，远程库的名字就是origin
  $ git remote add origin git@github.com:${GitHub账户名}/${远程仓库名称}.git
  
  # 4.下一步，就可以把本地库的所有内容推送到远程库上
  # 把本地库的内容推送到远程，用git push命令，实际上是把当前分支master推送到远程
  # 由于远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令
  $ git push -u origin master
  
  以下是github的官方提示(对应step3-4)：
  git remote add origin https://github.com/xzh634613957/my_demo_repository.git
  git branch -M main
  git push -u origin main
  
  # 5.从现在起，只要本地作了提交，就可以通过以下命令把本地master分支的最新修改推送至GitHub
  $ git push origin master
  
  # 6.删除远程库
  # 此处的“删除”其实是解除了本地和远程的绑定关系，并不是物理上删除了远程库。远程库本身并没有任何改动
  # 先用git remote -v查看远程库信息
  $ git remote -v
      origin	git@github.com:xzh634613957/my_demo_repository.git (fetch)
      origin	git@github.com:xzh634613957/my_demo_repository.git (push)
  # 然后，根据名字删除，比如删除origin
  $ git remote rm origin
  
  
  ```

  

- 拉取到本地

  ```shell
  git pull origin master
  ```

- 查看分支

  ```shell
  git branch -a
  ```

  