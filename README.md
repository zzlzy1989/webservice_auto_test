一、项目描述：

        webservice_auto_test 接口自动化测试框架
引言

        部署环境时，首先执行requirements.txt，命令如下:
        导出环境中的第三方库：pip freeze > requirements.txt
        新的服务器导入第三方库：pip -r install requirements.txt

二、各个模块简介

    1、Common封装的常用的方法

        contants 方法为定义路径方法，获取文件路径和其他参数的路径
        do_excel 操作excel方法

        context 上下文处理，正则的通用类，调用replace进行替换，目前主要用于操作excel，对excel中的参数进行匹配和替换
        config 完成配置文件的读取
        do_mysql 操作数据库，完成与MySQL数据库的交互

        HTMLTestRunnerNew 生成测试报告模板
        logger 日志处理

    2、Config    配置文件

        global.conf 全局变量，控制使用线上还是test的环境开关
        online.conf 线上环境的配置  包含接口地址，数据库地址和HTMLTestRunnerNew的配置信息
        test.conf   测试环境配置

    3、Log

        存放日志文件

    4、Reports

        report.html 生成的测试报告文件

    5、TestCases

        run.py  使用unittest，调用defaultTestLoader方法，加载discover，用来查询某个文件夹下以test_开头的.py结尾的文件，用来执行所有的测试用例，并生成测试报告

    6、TestDatas

        cases.xlsx 维护测试用例

三、git常用命令

    git clone 拷贝副本到本地
    git status 查看未被追踪的文件
    git add 追踪文件F
    git commit -m "注释" 提交文件
    git push 推到远程
    git branch 查看本地所有的分支
    git branch -a 查看所有的远程分支
    git checkout -b branch1 创建分支
    git checkout master 切换分支
    git push --set-upstream origin branch1 将分支推送到远程

四、pycharm操作git

    1、安装完成git以后，在setting中设置git.exe文件，在安装目录中找到git.exe文件，然后就可以在pycharm中操作git了
    2、在右下角有git的分支结构，local branchs代表本地分支结构，remot branchs远程分支结构
    3、在开发新的代码时，首先创建一个分支，或者是用本地分支
    4、在使用本地分支时，查看本地和远程分支是否一致，如果不一致，将本地分支提交或marge远程分支结构到本地，然后进行编写代码！
    5、New Branch,创建一个新的分支，以当前获取的分支代码为基准！
    6、修改代码并进行提交，右键Git>Commit Files，查看修改记录，点击commit and push进行提交；提交完成后就可以在GitHub网站中进行合并分支

五、Jenkins持续集成

    1、安装jenkins，方式1：官网下载jenkins.war，java -jar jenkins.war，命令行停掉，服务会停掉 --httpPort=8888修改端口号
    2、下载jenkins.war包，加到tomcat中，进行控制，启动tomcat时，jenkins自动启动 --server.xml修改端口号
    3、windows中，安装pgk，jenkins.msi文件，安装完成后，自动加入服务中，服务中加入jenkins服务，自动启动（修改端口号：文件找到jenkins
        ，修改httpPort=8888）
    4、默认安装目录为D:\Jenkins
    5、持续集成工具还有hudson，jenkins
    6、jenkins主要做，拿到开发的最新代码部署到服务器上
    7、系统设置--全局工具配置（配置git地址，安装版本）--插件管理（enkins安装插件：HTML Publisher/git/Email Extension）
    8、mater-slave主从构建，分布式构建，web ui。修改jenkins配置，可以使用grouvy
    9、在jenkin配置中，添加：构建》执行Windows批处理命令》
        命令：pip install -r requirements.txt --user
        python TestCases/run.py
        添加：构建后操作 Publis HTML Reports： HTML directory to archive（文件路径）Index page[s]（页面地址）Report title（标题）
        添加：Editable Extended Email Publisher 》》》 Attachments（附件）Reports/report.html,
            Attach Build Log配置Do Not Attach Build Log
    10、点击构建，即可进行自动构建项目！