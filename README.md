Automatic_refresh
=================

Git 多仓库更新工具

##用途：

当你的一个文件夹里面有N个Git仓库， 而你又想给每个仓库全部都执行 `git pull`的时候， 这个小东西就是你救星。
	
## 使用
1. 切换到所有git仓库的父级目录
2. `python autoPull.py`
3. 坐等它自动弄完

##功能

1. 会在你执行python脚本的那个目录里面创建一个log文件夹
2. 能够自动读取仓库的默认分支
3. 会以每个git仓库名创建一个log文件
4. 当遇到版本冲突等问题的时候， 会把仓库的名字写入`error.log`


## 反馈
Contact Me: dongtiangche@gmail.com