=================
EZLog
=================


**Easy Blog System**


简介
======

EZLog是用 `Django <https://www.djangoproject.com/>`_ 开发的个人博客系统，
也可以用来做个人网站。欢迎试用！


示例站点
=========

- http://ezlog.sinaapp.com/
- http://hoiyeung.sinaapp.com/


特性
======

- `响应式的WEB页面设计 <http://en.wikipedia.org/wiki/Responsive_web_design>`_, 能够自适应不同尺寸的屏幕

- 通过标签和分类来管理文章

- 可选择使用 Markdown 或者 HTML 撰写博客，并分别提供对应的编辑器组件

- 集成 `多说社会化评论框 <http://duoshuo.com/>`_

- 集成 `Google Analytics <http://www.google.cn/intl/zh-CN_ALL/analytics/>`_

- 最近访客跟踪

- 使用 `Django Grappelli <https://github.com/sehmaschine/django-grappelli>`_
  优化后台管理界面

- 使用 `Django FileBrowser <https://github.com/sehmaschine/django-filebrowser>`_
  管理上传的文件

- 层次化的页面管理

- 可配置的站点导航栏

- 通过WEB界面配置站点参数

- 站点地图


依赖的Python模块
================

- Django==1.4.1

- pyquery
  
- lxml(needed by pyquery)

- django-taggit(SAE环境下需要修改代码)

- django-grappelli

- django-filebrowser

- PIL(needed by django-filebrowser, PIL needs libjpeg libjpeg-dev)

- South

- django-compressor

- django-mptt

- Markdown


测试运行
========

- 获取EZLog代码::

    $ git clone https://github.com/wonderbeyond/ezlog.git

- 安装依赖模块::

    $ cd ezlog
    $ pip install -r requirements.txt

- 初始化数据库::

    $ mkdir data
    $ make syncdb

  请在命令执行过程中根据提示创建超级用户。

- 搜集静态文件到 settings.STATIC_ROOT 文件夹::

    $ mkdir static
    $ make collectstatic

OK，现在可以测试运行了。
这里使用Django提供测试服务器来运行，请不要应用于生产环境中！
生产环境下的部署方案请参考Django文档: https://docs.djangoproject.com/en/1.4/howto/deployment/

::

    $ python manage.py runserver 8000

如果看到如下提示::

    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

说明网站运行成功！打开浏览器，访问 http://127.0.0.1:8000/ 查看效果，
访问 http://127.0.0.1:8000/admin/ 可执行后台管理, 
需要使用刚刚创建的superuser登录。

在实际使用时，请访问 http://localhost:8000/ezsettings/
并根据需要修改站点参数，在admin管理界面可以看到该链接。

.. Note:: 如果你在测试或部署EZLog时遇到了问题，
    可以先看看我的 开发笔记_
    里面有没有提到对应问题的解决方法。
    也可以在新浪微博上 `@workwonder <http://weibo.com/wber>`_ 向我反馈,
    或者在这里留言: http://ezlog.sinaapp.com/20/#comments.


配置
====

设置 sites.site
-----------------

为了保证各个模块获得正确的信息（比如站点地图要生成网站的链接），
请访问 http://localhost:8000/admin/sites/site/,
然后把域名 *example.com* 修改为你正在使用的域名。

Django settings
----------------

EZLog项目中，settings.py被拆分成一个包，由__init__.py负责导入所有设置。

- base.py: 提供基本设置，优先级最低

- for_heroku.py: 提供针对Heroku环境的设置

- for_sae.py: 提供针对SAE环境的设置

- dev.py: 提供特定于测试环境下的设置

- production.py: 提供特定于生产环境下的设置

- switcher.py: 用来切换生产环境和测试环境的设置

- local.py: 提供你针对自己网站的设置，优先级最高

.. _开发笔记: https://github.com/wonderbeyond/ezlog/blob/master/doc/dev_notes.rst
