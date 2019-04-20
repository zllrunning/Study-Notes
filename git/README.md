### 配置
- git config --global user.name zllrunning
- git config --global user.email zllrunning@gmail.com

- git config --list --global   查看global配置

### 建git仓库
- git init repo

touch readme

- git add readme   
- git commit -m'Add readme'　
可以一条语句　git commit -am ' Add readme'

git status
git log


git add -A  
git add -u 一次性添加多个更改的文件　　只能添加已经跟踪的

### 文件重命名
git mv README.md readme.md
git commit -m'change readme file name'

### git log的一些用法
- git log --oneline　　一行简洁的显示
- git log -n2　只显示最近的两个commit
- git log -n2 --oneline 当然可以组合使用

### 图形化界面
gitk



**git cat-file -t bdc12a90      -t 查看类型**
**git cat-file -p bdc12a90      -p 查看内容**


**commit tree blob关系  看看11节**


### 分离头指针的注意事项



### 进一步理解HEAD和branch

HEAD 其实具体指向的是某一个　commit
git diff 
- git diff HEAD HEAD^
- git diff HEAD HEAD^^   其中^表示父级，^^表示父级的父级
- git diff HEAD HEAD～２　就可以代替　^^

### 新建分支
- git branch dev 新建分支
- git checkout dev　切换至该分支
上述可合为一句
- git checkout -b dev　　新建分之，并切换到dev分支
- 可使用　git branch　列出所有分支，及处在哪个分支


git push origin 本地分支名:远程分支名
如果远程没有该分支，远程会新建该分支

### 怎么删除不需要的分之

git branch -d haha
没有merge的可能删不掉，需要
git branch -D haha

### 修改commit的message
- git commit --amend
修改最近一次的message

- git rebase -i 1b3ce1e5a075eb2d13711e5d5
变基操作　　修改之前的commit message 
注意:　哈希值取它父亲的哈希值，然后编辑，具体参见１６课

reword 模式
### 合并连续的多个commit为一个commit
- git rebase -i 1b3ce1e5a075eb2d13711e5d5
squash 模式

### 合并不连续的几个commit为一个commit
没搞好

### 暂存区和HEAD文件作比较
git diff --cached

### 暂存区和工作区文件作比较
git diff
默认比较工作区和暂存区差异，*整个工作区内容*

git diff -- readme.md　　　　**-- 后面有个空格**
只比较暂存区和工作区readme.md文件的差异
git diff -- readme.md　test.m 比较指定的多个文件

### 暂存区恢复成和HEAD一样
应用案例：工作区的修改比暂存区的好，想把暂存区恢复成HEAD一致的

git reset HEAD

### 如何让工作区的文件恢复为和暂存区一样

git checkout test.m

### 如何取消暂存区部分文件的修改
git reset HEAD -- readme.md

### 消除最近的几次提交

- git reset --hard a40aa5b98　
HEAD is now at a40aa5b　头指针指向了这个commit，暂存区和工作区都恢复到了这个commit的状态(*比较危险的操作*)

### 看看不同提交指定文件的差异
git diff 9fad38d0a1f a40aa5b98f -- readme.md

### 正确删除文件的方法
- git rm butterfly.png

### 紧急任务加塞怎么处理
- git stash　压入stash
- git stash list 列出stash列表
- git stash apply 只能出stash,但是不弹出
- git stash pop　恢复现场且弹出（删除）这个stash


### 如何指定不需要git管理的文件
添加　　.gitignore  文件

### 已经跟踪的文件，如何使用.gitignore 取消跟踪
1. 修改　.gitignore 
2. git rm -r --cached data/Hand/

### git仓库备份
- git clone  file:///home/zll/Desktop/for_git/.git zhineng_nobare.git
- git clone **--bare** file:///home/zll/Desktop/for_git/.git zhineng.git

- git remote -v 查看
- git remote add zhineng file:///home/zll/Desktop/zhineng.git
- git push --set-upstream zhineng master

### git clone 自己的仓库后　git push 需要账号密码
如　Username for 'https://github.com':
解决方案：
- git remote set-url origin git+ssh://git@github.com/username/repo.git

### 本地仓库同步到github
添加github远端

- git remote add github git@github.com:zllrunning/for_git.git
- git fetch github master
- git merge github/master
- git push github master
---
- git branch -b git_commands github/git_commands 
以远端分支建立本地分支

### pull request
- 克隆代码到本地
git clone https://github.com/ZhaoJ9014/face.evoLVe.PyTorch.git
- 创建一个修改分支
git checkout -b fix_iter_loader_bug
- 对文件进行修改
- 提交修改，commit
git commit -am 'fix iter bug'
- 由于没有直接push到origin的权限，我们需要先对仓库进行fork，然后在本地添加一个新的推送地址
git remote add upstream git@github.com:zllrunning/face.evoLVe.PyTorch
- 推送本地分支到自己的face.evoLVe.PyTorch fork库
git push upstream fix_iter_loader_bug
- 到github网页pull request


### 不同人修改了不同文件，或者同一文件的不同位置
- git fetch 
- git merge
- git push

### 不同人修改了同一文件的相同位置 36讲
- git pull 
- 修改冲突的地方
- git commit -am'to do'
- git push github

### 同事变更了文件名和文件内容如何处理
- git pull

### 禁止向集成分支使用　git push -f 操作
### 禁止向集成分支执行变更历史的操作


### github 高级搜素
face detection in:readme stars:>1000
face detection in:readme filename:model.py
具体的可以在github help页面查看
条件可以叠加使用
















