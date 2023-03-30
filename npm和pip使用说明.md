# NPM

如查看xxx包的最新版本信息：npm view xxx versions 或者 npm info xxx

使用npm安装指定版本的包：npm i xxx@4.11.0 --save-dev

使用npm升级指定版本的包：npm update xxx --save-dev

安装xxx最新版本的包：npm i xxx@latest --save-dev

使用npm查看已安装的包列表：npm list

使用npm查看已安装某一指定包的版本信息：npm list xxx

npm错误——npm ERR! code ERESOLVE 解决方法

在安装组件的时候出现以上问题，npm版本问题报错

解决方法：

在命令后面加上

    --legacy-peer-deps

# PIP

更新升级pip：

    python3 -m pip install --upgrade pip
    pip install --upgrade pip

安装包

    pip install 安装包名

pip安装指定版本号的包

    pip install zipp==3.5.0

查看某包是否安装

    pip show --files 安装包名

pip检查哪些包需要更新

    pip list --outdated

pip升级包

    pip install --upgrade 要升级的包名

pip升级包到指定版本号 

    pip install --upgrade 包名称==版本号

pip卸载包

    pip uninstall 要卸载的包名

pip参数解释

    pip --help

pip列出所有的包

    pip list

一次性安装多个包

    pip install -r requeriments.txt