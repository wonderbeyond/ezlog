EZLog 开发笔记
==============

这里记录在该系统开发过程中遇到过的问题及解决方法。


解决virtualenv中安装PIL出现的 `IOError: decoder jpeg not available` 问题
-------------------------------------------------------------------------

参考资料: http://ubuntuforums.org/showthread.php?p=10811107

解决方法为:

下载PIL源码(http://www.pythonware.com/products/pil/),
编辑 setup.py, 找到 `add_directory(library_dirs, "/usr/lib")` 一行,
在下面添加一行: `add_directory(library_dirs, "/usr/lib/i386-linux-gnu")`.
然后在虚拟环境中执行 setup.py 安装PIL.
另外, 系统需要安装 libjpeg libjpeg-dev 相关库.


解决使用MySql数据库时的syncdb错误
----------------------------------

使用MySql数据库时, 如果在django模型的Meta类中设置了中文的 `verbose_name`,
syncdb时可能出现 `Incorrect string value` 的错误.

参考http://www.haogongju.net/art/901598, 解决方法如下:

删除了之前直接创建的 ezlog 数据库, 重新使用以下SQL创建::

    create database ezlog DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

如果直接修改的话, 则对已有的表没有影响::

    ALTER DATABASE ezlog CHARACTER SET utf8 COLLATE utf8_general_ci;

然后重新授权::

    grant ALL PRIVILEGES ON ezlog.* to wonder@localhost;


部署到SAE
----------

过程概要

- 上传代码(打包依赖的python包到virtualenv.bundle.zip)

- 导入MySQL数据

- 在SAE Storage管理页面创建名为base的domain.


从MySQL导出数据
----------------

::

    mysqldump --skip-add-locks -u wonder ezlog -p > ~/lab/ezlog.sql


admin界面找不到模板
-------------------

由于把依赖的包压缩到了一个zip文件由SAE环境导入,
但是TEMPLATE_LOADERS中设置的app_directories.Loader不再从zip中寻找模板了.
参考了DPress代码后, 在TEMPLATE_LOADERS中添加了eggs.Loader, 解决模板寻找问题.

同时发现存在模板引用混乱问题, 比如grappelli在INSTALLED_APPS明明排得靠前,
但是admin管理界面还是优先引用了django.contrib.admin提供的模板.

经考察, 这是由于 grappelli 等放到 virtualenv.bundle.zip
中的额外包是通过 eggs.Loader 加载的, 要把 eggs.Loader 放在 app_directories.Loader 之前以获得更高的优先级.


对BootStrap的定制
------------------

::

    body {
        font-size: 13px;
        line-height: 18px;
    }
